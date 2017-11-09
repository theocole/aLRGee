import xml.etree.ElementTree as ET
import pprint

import sys


def parse_exon_positions(lrg_file):
    """
    Parse the LRG XML file and get the positions of the exons using LRG
    coordinate system, returning a dictionary of relative exon positions
    with the following structure (and start/stop positions on each genome
    build.

    Usage
    -----
    xml_parser("LRG_9.xml")
     -->
        sample_dict = {
        'lrg_id': "LRG_X",
        'transcript1': {
            'relative_exon_positions': {
                'exon1': {
                    'start': 128,
                    'stop': 345
                }
                'exon2': {
                    'start': 745,
                    'stop': 923
                }
                'exon3': {
                    'start': 1184,
                    'stop': 1592
                }
                'exon4': {
                    'start': 1808,
                    'stop': 2140
                }
                'exon5': {
                    'start': 2781,
                    'stop': 3019
                }
            }
        }
        'transcript2': {
            'relative_exon_positions': {
                'exon1': {
                    'start': 80,
                    'stop': 194
                }
                'exon2': {
                    'start': 555,
                    'stop': 801
                }
                'exon3': {
                    'start': 958,
                    'stop': 1104
                }
            }
        }
        'build_GRCh37': {
            'mapping_start': 187429875,
            'mapping_stop': 187431770,
        }
        'build_GRCh38': {
            'mapping_start': 179354041,
            'mapping_stop': 179357191,
        }

    }

    """  

    position_dict = {}

    lrg_tree = ET.parse(lrg_file)

    lrg_root = lrg_tree.getroot()
    fixed, updatable = lrg_root.getchildren()

    lrg_id = fixed.find("id").text
    position_dict["lrg_id"] = lrg_id
    print lrg_id

    transcripts = lrg_root.iter("transcript")
    for transcript in transcripts:
        if 'name' in transcript.attrib:
            transcript_name = transcript.attrib['name']
            print transcript_name
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

    return position_dict

pprint.pprint(parse_exon_positions(sys.argv[1]))