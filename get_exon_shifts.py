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
            #else:
            #print"Error gene name not found"
        '''
        ####
    def xml_parser():
=======
    def xml_parser(lrg_file):
>>>>>>> 2838f2c7832ea97cdb21aabe106aa9699b220401
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
        pass

    def display_results():
        """
        Takes df of relative exon positions and absolute genome coords and displays
        on html template.
        """
        pass
