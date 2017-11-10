import sys
import argparse
import urllib2
import pandas
from jinja2 import Environment, FileSystemLoader
import datetime
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import re

import pprint

"""
Command line tool to get LRG file,


Usage:
------

alrgee.py <gene_name> -e <exon_of_interest> [<exons_before>] [<exons_after>]
"""


def get_exon_shifts():
    """
    Run through the whole process: take a gene name and output HTML report
    of exon position shifts between the two genome builds.
    """

    args = parse_args()
    lrg_file_url = xml_scraper(args['gene_name'])
    position_dict = xml_parser(lrg_file_url)
    results_dict = plot_exon_shifts(position_dict)

    pprint.pprint(results_dict)


def parse_args():

    # creating flags for arguments
    # parser = argparse.ArgumentParser()
    # parser.add_arguments('-n', action='store',
    #                      dest='exon_name', help='LRG gene name')
    # parser.add_arguments(
    #     '-e', action='store', dest='exon_number', help='Insert exon number of interest')
    # parser.add_arguments('-b', action='store', dest='exon_before',
    #                      help='Insert exon no. which comes before exon of interest')
    # parser.add_arguments('-a', action='store', dest='exon_after',
    #                      help='Insert exon no. which comes after exon of interest')

    # results = parser.parse.args()

    parser = argparse.ArgumentParser(description="Take gene name and exons of interest.")
    parser.add_argument(
        '-n', action='store', dest='gene_name', help='HGNC gene name.'
    )
    parser.add_argument(
        '-e', action='store', dest='exon_of_interest', help='Exon you would like to display a shift calculation for.'
    )
    parser.add_argument(
        '-b', action='store', dest='exons_before', help='The number of exons before your exon of interest.'
    )
    parser.add_argument(
        '-a', action='store', dest='exons_after', help='The number of exons after your exon of interest.'
    )

    command_args = parser.parse_args()
    return vars(command_args)


def xml_scraper(gene):

    lrg_response = urllib2.urlopen("https://www.lrg-sequence.org/LRG")
    lrg_list_html = lrg_response.read()

    lrg_soup = BeautifulSoup(lrg_list_html, 'html.parser')

    gene_cell = lrg_soup.find("td", text=re.compile("^" + gene + "$"))

    gene_row = gene_cell.find_parent("tr")

    gene_xml_link = gene_row.find("a", text=re.compile("^LRG_\d+$"))
    gene_xml_href = gene_xml_link['href']

    return gene_xml_href


def xml_parser(lrg_file_url):
    """
    Parse the LRG XML file and get the positions of the exons using LRG
    coordinate system, returning a dictionary of relative exon positions
    with the following structure (and start/stop positions on each genome
    build.

    """

    position_dict = {}

    lrg_tree = ET.ElementTree(file=urllib2.urlopen(lrg_file_url))

    lrg_root = lrg_tree.getroot()
    fixed, updatable = lrg_root.getchildren()

    lrg_id = fixed.find("id").text
    position_dict["lrg_id"] = lrg_id

    transcripts = lrg_root.iter("transcript")
    for transcript in transcripts:
        if 'name' in transcript.attrib:
            transcript_name = transcript.attrib['name']
            transcript_dict = position_dict[transcript_name] = {}

            transcript_exons = [
                x for x in transcript.findall("exon") if "label" in x.attrib
            ]

            for exon in transcript_exons:
                exon_label = "exon" + exon.attrib["label"]
                exon_position_dict = transcript_dict[exon_label] = {}
                for coords in exon:
                    if coords.attrib["coord_system"] == lrg_id:
                        exon_position_dict["start"] = coords.attrib["start"]
                        exon_position_dict["end"] = coords.attrib["end"]

    mapping_annotation = None

    annotation_sets = updatable.findall("annotation_set")
    for annotation_set in annotation_sets:
        if annotation_set.attrib["type"] == "lrg":
            mapping_annotation = annotation_set

    assert mapping_annotation is not None

    for mapping_coords in mapping_annotation.findall("mapping"):
        build_name = "build_" + \
            mapping_coords.attrib["coord_system"].split('.')[0]
        build_dict = position_dict[build_name] = {}
        build_dict["start"] = mapping_coords.attrib["other_start"]
        build_dict["end"] = mapping_coords.attrib["other_end"]

    return position_dict


def plot_exon_shifts(position_dict):
    def calc_genomic_position(exon_num, hg_18_start, hg_18_stop, hg_19_start, hg_19_stop, exon_start, exon_stop):
        hg18ex_start = (hg_18_start+exon_start)
        hg18ex_stop = (hg_18_stop+exon_stop)
        hg19ex_start = (hg_19_start+exon_start)
        hg19ex_stop = (hg_19_stop+exon_stop)
        pos_shift = hg19ex_start - hg18ex_start
        return [exon_num, hg18ex_start, hg18ex_stop, hg19ex_start, hg19ex_stop, pos_shift]


    transcripts = []
    transcripts_and_exons = []
    exon_positions = []
    resultsdict ={}

    for key, value in position_dict.iteritems():
        if key.startswith("build_GRCh38"):
            build_38 = value
        if key.startswith("build_GRCh37"):
            build_37 = value
        if key.startswith("lrg_id"):
            LRG_id = value
        if key.startswith("t"):
            transcripts.append([str(key), value])


    for key, value in build_38.iteritems():
        if key.startswith("start"):
            build_19_start = int(value)
        if key.startswith("end"):
            build_19_stop = int(value)


    for key, value in build_37.iteritems():
        if key.startswith("start"):
            build_18_start = int(value)
        if key.startswith("end"):
            build_18_stop = int(value)


    for entry in transcripts:
        transcript_number = entry[0]
        exon_dict = entry[1]
        for key, value in exon_dict.iteritems():
            exon_number = key
            exon_start_stop = value
            transcripts_and_exons.append([transcript_number, exon_number, value])


    for entry in transcripts_and_exons:
        transcript = entry[0]
        exon_positions.append([transcript])
        exon_start_stop_dict = entry[2]
        exon_num = entry[1]
        for entry in exon_positions:
            if transcript in entry:
                index = exon_positions.index(entry)
        for key, value in exon_start_stop_dict.iteritems():
            if key == "start":
                start = value
            if key == "end":
                stop_coord = value

                exon_positions[index].append([exon_num, start, stop_coord])


    for entry in exon_positions:
        transcript = entry[0]
        exons = entry[1:]
        for detail in exons:
            exon_num = detail[0]
            exon_start = int(detail[1])
            exon_stop = int(detail[2])
            dataline = calc_genomic_position(exon_num, build_18_start, build_18_stop, build_19_start, build_19_stop, exon_start, exon_stop)
            if transcript not in resultsdict:
                resultsdict[transcript] = [dataline]
            else:
                resultsdict[transcript].append(dataline)

    return resultsdict


def display_results(resultsdict):
    """
    Takes df of relative exon positions and absolute genome coords and displays
    on html template.
    """
    for key, value in args.iteritems():
        if key == "exon_of_interest":
            if value is not None:
                exon_of_interest = int(value)
            else:
                exon_of_interest = "blank"
        if key == "exons_before":
            if value is not None:
                exons_before = int(value)
            else:
                exons_before = 0
        if key == "exons_after":
            if value is not None:
                exons_after = int(value)
            else:
                exons_after = 0
        if key == "gene_name":
            gene_name = value

    dataframes = []
    transcripts = []

    if exon_of_interest != "blank":
        for key, value in resultsdict.iteritems():
            transcript = key
            transcripts.append(transcript)
            headers = ["Exon number", "GrCh37_Start", "GrCh38_Start", "GrCh37_stop", "GrCh38_stop", "Positional Shift"]
            newlist = []
            exons_before_list = []
            exons_after_list = []

            for entry in value:
                exon_number = int(entry[0].strip("exon"))
                if exon_number == exon_of_interest:
                    EOI = [entry]
                if exon_number > exon_of_interest:
                    if exon_number <= (exon_of_interest + exons_after):
                        exons_after_list.append(entry)
                if exon_number < exon_of_interest:
                    if exon_number >= (exon_of_interest - exons_before):
                        exons_before_list.append(entry)
            if len(exons_before_list) >= 1:
                if len(exons_after_list) >= 1:
                    newlist = exons_before_list+EOI+exons_after_list
                else:
                    newlist = exons_before_list+EOI
            else:
                newlist = EOI
            df = pandas.DataFrame(newlist, columns=headers)
            myfinisheddata = df.to_html(index=False)
            dataframes.append(myfinisheddata)

    else:
        for key, value in resultsdict.iteritems():
            transcript = key
            transcripts.append(transcript)
            headers = ["Exon number", "GrCh37_Start", "GrCh38_Start", "GrCh37_stop", "GrCh38_stop", "Positional Shift"]
            newlist = []
            for entry in value:
                newlist.append(entry)

            df = pandas.DataFrame(newlist, columns=headers)
            myfinisheddata = df.to_html(index=False)
            dataframes.append(myfinisheddata)




    now = datetime.datetime.now()

    current_date = now.strftime("%d-%m-%Y")

    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template("xml_report_template.html")
    # define what to pass to the template
    template_vars = {"title": "Results for "+ gene_name, "transcripts": transcripts,"data": dataframes,}
    # pass the template vars to the template
    html_out = template.render(template_vars)
    # write to a html file named of the current date
    file_out = open(current_date + ".html", "w")
    file_out.write(html_out.replace(
        " border=\"1\" class=\"dataframe\"", ""))
    file_out.close()
