# aLRGee 
Program written to output differences between exon positions for genome builds within LRG files.

Written by: Theo Cole, Rebecca Forrester and Natasha Pinto 
************
Synopis
************
aLRGee is a command line tool developed to comapare LGR files with exon builds to investigate the differences between exon positions to aid in varaint investigation in a clinical setting.

##############################################################################################
Running aLRGee from command line 
##############################################################################################

To run the tool in command line: 

	>>  python aLRGee -n <gene name> -e <exon of interest> -b <Number of exons before EOF*> -a <Number  of exons after the EOF*>

EOF= Exon of interest 

Required arguments: 
-n -e
Optional arguments:
-b -a 

For full description of arguments refer to the help page 

	>> python aLRGEE --help


Example:


	eg:
		>> python aLRGEE -n NF1 -e 5 -b 1 -a 3

##################################################################################################
REQUIREMENTS
##################################################################################################

To run the tool you will need to have python 2.6 installed, as the some of the modules used require python 2.6 or over. 

Refer to https://www.python.org/download/releases for instructions on how to update/dowload python 2.6 or over 

###################################################################################################
aLRGee explained
###################################################################################################

def main():


 Example:

    args = parse_args()
    lrg_file_url = xml_scraper(args['NF1'])
    position_dict = xml_parser(lrg_file_url)
    results_dict = plot_exon_shifts(position_dict)



Function: def parse_args():
###########################

 The add_argumnets method is used to create flags for arguments; a help page with description of each flag is created simultaneously. The help page can be accessed using --help.
   action- The action to be taken when the flag is encountered, in this instrance the flag shold be stored.
   dest- refers to the attribute associated to the flag
   help- provides a brief description of the function of the flag
   required- Detting it as TRUE, makes the flag a required command line option. 


	>> parser = argparse.ArgumentParser(description="Take gene name and exons of interest.")
    
    >> parser.add_argument(
        '-n', action='store', dest='gene_name', required='TRUE', help='HGNC gene name.'
    )

Function: def xml_scraper(gene):
#################################

xml_scrapper function uses urllib2 to open the LRG sequence URL and puts the html in a dictionary called lrg_list_html. 
The BeautifulSoup library is used to pull data out of the html file and transfer it into another dictionary called lrg_soup. 
Then lrg.soup.find searches for the tag "td" and the absolute gene name associated with the tag:

	>> gene_cell = lrg_soup.find("td", text=re.compile("^" + NF1 + "$"))

If the function is unable to find the gene of interest it will output an error

	>> "Could not find gene!"

This will indicate the user that a LRG file is not available for their gene of interest; the tool will automatically abort.

If the gene is found user will receive this output:
	> "Found gene!"

The tool will then proceed to access the associated XML file (href), by finding the LGR file tag "a". The output will be inserted into "gene_xml_href". If the tool fails to find the xml file it will produce a message:

	>> "Could not find a valid LRG file associated with gene."

If the associated xml file is found it will print:

	>> "LRG file found at:", NF1_xml_href

Function- def xml_parser(lrg_file_url):
######################################

 Parse the LRG XML file and get the positions of the exons using LRG coordinate system, returning a dictionary of relative exon positions with the following structure (and start/stop positions on each genome build.


