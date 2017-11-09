import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import urllib2
import re


def xml_scraper(gene):
    #1 access www.lrg-sequence.org/LRG
    lrg_response = urllib2.urlopen("https://www.lrg-sequence.org/LRG")
    lrg_list_html = lrg_response.read()

    lrg_soup = BeautifulSoup(lrg_list_html, 'html.parser')

    gene_cell = lrg_soup.find("td", text=re.compile("^" + gene + "$"))

    gene_row = gene_cell.find_parent("tr")

    gene_xml_link = gene_row.find("a", text=re.compile("^LRG_\d+$"))
    gene_xml_href = gene_xml_link['href']

    lrg_xml_tree = ET.ElementTree(file=urllib2.urlopen(gene_xml_href))
    root = lrg_xml_tree.getroot()
    print root.tag, root.attrib


    #find table row with genename = gene

    # copy link location from LRG_ID column link

xml_scraper("NF1")