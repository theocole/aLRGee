import xml.etree.ElementTree as ET

tree = ET.parse("parse-test/LRG_9.xml")
root = tree.getroot()

for exon in root.iter("exon"):
    print exon.attrib


with open("parse-test/LRG_9.xml", "r") as lrg_9:
    for line in lrg_9:
        if "mapping coord_system=\"GRCh37.p13\"" in line:
            print line.split(" ")