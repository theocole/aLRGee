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

    def xml_parser():
        """
        Take XML file and return dict of relative exon positions and start and
        stop positions for both genome builds.

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
        pass

    def display_results():
        """
        Takes df of relative exon positions and absolute genome coords and displays
        on html template.
        """
        pass
