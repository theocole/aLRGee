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
hjgjjgjg

##################################################################################################
REQUIREMENTS
##################################################################################################

To run the tool you will need to have python 2.6 installed, as the some of the modules used require python 2.6 or over. 

Refer to https://www.python.org/download/releases for instructions on how to update/dowload python 2.6 or over 

###################################################################################################
aLRGee explained
###################################################################################################

