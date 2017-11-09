import xml.etree.ElementTree as ET
import pprint

import sys


def parse_exon_positions(lrg_file):
    """
    Parse the LRG XML file and get the positions of the exons using LRG
    coordinate system, returning a dictionary of relative exon positions
    with the following structure (and start/stop positions on each genome
    build.
    """

    position_dict = {}

    lrg_tree = ET.parse(lrg_file)

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


pprint.pprint(parse_exon_positions(sys.argv[1]))
