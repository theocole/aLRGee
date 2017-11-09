import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import urllib2
import re


def xml_scraper(gene):
    #1 access www.lrg-sequence.org/LRG
    lrg_response = urllib2.urlopen("https://www.lrg-sequence.org/LRG")
    lrg_list_html = lrg_response.read()

    lrg_soup = BeautifulSoup(lrg_list_html, 'html.parser')

    gene_row = lrg_soup.findAll("td", text=re.compile("^" + gene + "$"))
    print gene_row


    #find table row with genename = gene

    # copy link location from LRG_ID column link

xml_scraper("NF1")