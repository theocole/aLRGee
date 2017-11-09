import pandas
from jinja2 import Environment, FileSystemLoader
import datetime

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

    def xml_parser(lrg_file):
        """
        Take XML file and return dict of relative exon positions and start and
        stop positions for both genome builds.

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
        pass

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

        test_dict = {"col1": [1,2], "col2": [3,4]}
        mydataframe = pandas.DataFrame(data=test_dict)
        mydataframe.head()

        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template("xml_report_template.html")
        template_vars = {"hello": mydataframe.to_html(), "title" : "This is the title"}
        html_out = template.render(template_vars)
        file_out = open(current_date+".html", "w")
        file_out.write(html_out)
        file_out.close()

        pass
