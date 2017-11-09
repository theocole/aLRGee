import sys
import argparse
import urllib2
import pandas
from jinja2 import Environment, FileSystemLoader
import datetime
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import re

"""
Command line tool to get LRG file,


Usage:
------

alrgee.py <gene_name> -b <build_number> -e <exon_of_interest> [<exons_before>] [<exons_after>]
"""


def get_exon_shifts(gene_name):
    """
    Run through the whole process: take a gene name and output HTML report
    of exon position shifts between the two genome builds.
    """
    lrg_file_url = xml_scraper(gene_name)
    position_dict = xml_parser(lrg_file_url)

    print(position_dict)


def parse_command_line_args():
    pass

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

def plot_exon_shifts():
    """
    Take dict of exon positions and absolute genome coords and put into pandas
    df.

    Filter out irrelevant information from the dict, ie only take the exons of
    interest.

    Also, set the user's build at this point to determine 'their' exon positions
    and the the shift they would like to know.
    """
    # take dictionaries from xml_parser and split dictionary into components
    # define arguements:
    # desired_exons = []
    # create empty data frame:

    """ |exon num | pos_start   |   pos_end  | relative shift |
        __________| hg18 | hg19 | hg18 | hg19|________________|
        |         |      |      |      |     |                |
        |         |      |      |      |     |                |
"""

    # for exon in desired_exons:
    # add data as a row in the data frame
    pass

def display_results():
    """
    Takes df of relative exon positions and absolute genome coords and displays
    on html template.
    """
    now = datetime.datetime.now()

    current_date = now.strftime("%d-%m-%Y")

    # defining the pandas dataframe
    test_dict = {"col1": [1, 2], "col2": [3, 4]}
    mydataframe = pandas.DataFrame(data=test_dict)
    mydataframe.head()

    # defining the html template
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template("xml_report_template.html")
    # define what to pass to the template
    template_vars = {"hello": mydataframe.to_html(),
                     "title": "This is the title"}
    # pass the template vars to the template
    html_out = template.render(template_vars)
    # write to a html file named of the current date
    file_out = open(current_date + ".html", "w")
    file_out.write(html_out)
    file_out.write(html_out.replace(
        " border=\"1\" class=\"dataframe\"", ""))
    file_out.close()

    pass


get_exon_shifts(sys.argv[1])