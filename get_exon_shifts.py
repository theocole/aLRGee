import sys 
import argparser
import urllib2
import pandas
from jinja2 import Environment, FileSystemLoader
import datetime
import xml.etree.ElementTree as ET

"""
Command line tool to get LRG file,


Usage:
------

alrgee.py <gene_name> -b <build_number> -e <exon_of_interest> [<exons_before>] [<exons_after>]
"""

def get_exon_shifts(cl_args):


    def take_gene_name():
        """
        Take a gene name and get the corresponding XML file from
        www.lrg-sequence.org/LRG"
        - Take gene name as arg
        - Return XML if gene name found in list, give user warning if gene
          not found
        """
        pass

<<<<<<< HEAD
<<<<<<< HEAD

        '''
    #!/usr/bin/python 
    #import sys 
    import argparser
    import urllib2
        
    #creating flags for arguments 
        parser.add_arguments('-n', action='store', dest='exon_name', help='LRG gene name')
        parser.add_arguments('-e', action='store', dest='exon_number', help='Insert exon number of interest')
        parser.add_arguments('-b', action='store', dest='exon_before', help='Insert exon no. which comes before exon of interest')
        parser.add_arguments('-a', action='store' dest='exon_after', help='Insert exon no. which comes after exon of interest')

        results = parser.parse.args()
        print 'exon_name     =', results.exon_name
        print 'exon_number   =', results.exon_number
        print 'exon_before   =', results.exon_before
        print 'exon_after    =', results.exon_after 

    
    def gene_name(name):
        page= urllib2.urlopen("www.lrg-sequence.org/LRG").read()
        print re.findall(name,page)
        print page.find(name)
    if 

    def take_gene_name(gene_name, exon_number, exon_before, exon_after):

          #if gene_name "www.lrg-sequence.org/LRG":
                #return XML 
=======
        #!/usr/bin/python
        # import sys
        # def take_gene_name ():
            #arg1[gene_name]
            #arg2[exon_of_interest]
            #arg3[exon_before]
            #arg4[exon_after]

            #if gene_name in URL:
                #return XML
>>>>>>> b31896e0cab6f13df2beebb4da64c6de75566f6d
            #else:
            #print"Error gene name not found"
        '''
        ####


    def xml_parser(lrg_file):
        """
        Take XML file and return dict of relative exon positions and start and
        stop positions for both genome builds.

        lrg_file must be a path to the XML file being used in this run of the
        program.

        Usage
        -----
        xml_parser("LRG_9.xml")
        ==> {gene_id: "SDHD",
             lrg_id: "LRG_9",
             rel_exons: {
                 exon1: {
                     start: 123,
                     stop: 543,
                 }
                 exon2: {
                     start: 876,
                     stop: 934
                 }
                 ...
             }
             build_37: {
                start: 1545693486,
                stop: 1634534988,
                exons: {
                    exon1: {
                        start: 157567567 + rel_exons[exon1]
                        stop: ...
                    }
                    ...
                }
             }
             build_38: {
                start: 1545234654,
                stop: 1634894564,
                exons: {
                    exon1: {
                        start: 157567567 + rel_exons[exon1]
                        stop: ...
                    }
                    ...
                }

            }

        """

        position_dict = {}

        tree = ET.parse(lrg_file)

        lrg_root = tree.getroot()
        fixed, updatable = lrg_root.getchildren()

        lrg_id = fixed.find("id").text
        position_dict["lrg_id"] = lrg_id

        lrg_exons = [x for x in root.iter("exon") if "label" in x.attrib]




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
        test_dict = {"col1": [1,2], "col2": [3,4]}
        mydataframe = pandas.DataFrame(data=test_dict)
        mydataframe.head()

        # defining the html template
        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template("xml_report_template.html")
        # define what to pass to the template
        template_vars = {"hello": mydataframe.to_html(), "title" : "This is the title"}
        # pass the template vars to the template
        html_out = template.render(template_vars)
        # write to a html file named of the current date
        file_out = open(current_date+".html", "w")
        file_out.write(html_out)
        file_out.write(html_out.replace(" border=\"1\" class=\"dataframe\"", ""))
        file_out.close()

        pass
