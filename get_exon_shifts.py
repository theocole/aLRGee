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

        #!/usr/bin/python 
        # import sys 
        # def take_gene_name ():
            #arg1[gene_name]
            #arg2[exon_of_interest]
            #arg3[exon_before]
            #arg4[exon_after]

            #if gene_name in URL:
                #return XML 
            #else:
            #print"Error gene name not found"
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
<<<<<<< HEAD
=======

>>>>>>> 1347d63255fb8139dcc63c87c065fc065824030b
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
        pass
