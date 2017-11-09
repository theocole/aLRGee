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

    tree = ET.parse(lrg_file)

    root = tree.getroot()
    fixed, changeable = root.getchildren()

    lrg_id = fixed.find("id").text
    position_dict["lrg_id"] = lrg_id

    lrg_exons = [x for x in root.iter("exon") if "label" in x.attrib]
    position_dict = {}

    for exon in lrg_exons:
        exon_label = "exon" + exon.attrib["label"]
        position_dict[exon_label] = {}
        for coords in exon:
            print coords.attrib["coord_system"]
            if coords.attrib["coord_system"] == lrg_id:
                position_dict[exon_label]["start"] = coords.attrib["start"]
                position_dict[exon_label]["end"] = coords.attrib["end"]


    return position_dict

pprint.pprint(parse_exon_positions(sys.argv[1]))