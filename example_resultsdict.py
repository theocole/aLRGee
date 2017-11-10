import sys
import argparse
import pandas
import datetime
from jinja2 import Environment, FileSystemLoader


def parse_args():

    parser = argparse.ArgumentParser(description="Take gene name and exons of interest.")
    parser.add_argument(
        '-g', action='store', dest='gene_name', help='HGNC gene name.'
    )
    parser.add_argument(
        '-e', action='store', dest='exon_of_interest', help='Exon you would like to display a shift calculation for.'
    )
    parser.add_argument(
        '-b', action='store', dest='exons_before', help='The number of exons before your exon of interest.'
    )
    parser.add_argument(
        '-a', action='store', dest='exons_after', help='The number of exons after your exon of interest.'
    )

    command_args = parser.parse_args()
    return vars(command_args)

args = parse_args()



results_dict = {'t1': [['exon56', 29685988, 29975734, 31358970, 31648716, 1672982],
        ['exon49', 29676139, 29965970, 31349121, 31638952, 1672982],
        ['exon58', 29701032, 29994396, 31374014, 31667378, 1672982],
        ['exon55', 29685499, 29975341, 31358481, 31648323, 1672982],
        ['exon48', 29670028, 29959854, 31343010, 31632836, 1672982],
        ['exon15', 29548869, 29838648, 31221851, 31511630, 1672982],
        ['exon14', 29546024, 29835837, 31219006, 31508819, 1672982],
        ['exon17', 29552114, 29841969, 31225096, 31514951, 1672982],
        ['exon16', 29550463, 29840286, 31223445, 31513268, 1672982],
        ['exon11', 29528430, 29818204, 31201412, 31491186, 1672982],
        ['exon10', 29528056, 29817878, 31201038, 31490860, 1672982],
        ['exon13', 29541470, 29831304, 31214452, 31504286, 1672982],
        ['exon12', 29533259, 29823090, 31206241, 31496072, 1672982],
        ['exon37', 29652839, 29942971, 31325821, 31615953, 1672982],
        ['exon36', 29592248, 29882058, 31265230, 31555040, 1672982],
        ['exon35', 29588730, 29878576, 31261712, 31551558, 1672982],
        ['exon34', 29587388, 29877234, 31260370, 31550216, 1672982],
        ['exon19', 29554237, 29844010, 31227219, 31516992, 1672982],
        ['exon18', 29553454, 29843403, 31226436, 31516385, 1672982],
        ['exon57', 29687506, 29977422, 31360488, 31650404, 1672982],
        ['exon30', 29576003, 29865838, 31248985, 31538820, 1672982],
        ['exon5', 29496910, 29786716, 31169892, 31459698, 1672982],
        ['exon4', 29490205, 29780095, 31163187, 31453077, 1672982],
        ['exon7', 29508729, 29798504, 31181711, 31471486, 1672982],
        ['exon6', 29508441, 29798208, 31181423, 31471190, 1672982],
        ['exon1', 29421946, 29712088, 31094928, 31385070, 1672982],
        ['exon39', 29657315, 29947217, 31330297, 31620199, 1672982],
        ['exon3', 29486029, 29775812, 31159011, 31448794, 1672982],
        ['exon2', 29483002, 29772845, 31155984, 31445827, 1672982],
        ['exon54', 29684288, 29974088, 31357270, 31647070, 1672982],
        ['exon38', 29654518, 29944558, 31327500, 31617540, 1672982],
        ['exon9', 29527441, 29817314, 31200423, 31490296, 1672982],
        ['exon8', 29509527, 29799384, 31182509, 31472366, 1672982],
        ['exon42', 29663654, 29953633, 31336636, 31626615, 1672982],
        ['exon43', 29664387, 29954301, 31337369, 31627283, 1672982],
        ['exon50', 29677202, 29967037, 31350184, 31640019, 1672982],
        ['exon51', 29679276, 29969133, 31352258, 31642115, 1672982],
        ['exon53', 29683979, 29973809, 31356961, 31646791, 1672982],
        ['exon52', 29683479, 29973301, 31356461, 31646283, 1672982],
        ['exon33', 29586051, 29875848, 31259033, 31548830, 1672982],
        ['exon32', 29585363, 29875221, 31258345, 31548203, 1672982],
        ['exon20', 29554542, 29844325, 31227524, 31517307, 1672982],
        ['exon21', 29556044, 29846184, 31229026, 31519166, 1672982],
        ['exon22', 29556854, 29846693, 31229836, 31519675, 1672982],
        ['exon23', 29557279, 29847101, 31230261, 31520083, 1672982],
        ['exon24', 29557861, 29847644, 31230843, 31520626, 1672982],
        ['exon25', 29559092, 29848908, 31232074, 31521890, 1672982],
        ['exon26', 29559719, 29849600, 31232701, 31522582, 1672982],
        ['exon27', 29560021, 29849932, 31233003, 31522914, 1672982],
        ['exon28', 29562630, 29852491, 31235612, 31525473, 1672982],
        ['exon29', 29562937, 29852740, 31235919, 31525722, 1672982],
        ['exon40', 29661857, 29951750, 31334839, 31624732, 1672982],
        ['exon41', 29663352, 29953192, 31336334, 31626174, 1672982],
        ['exon46', 29665723, 29955524, 31338705, 31628506, 1672982],
        ['exon47', 29667524, 29957364, 31340506, 31630346, 1672982],
        ['exon44', 29664838, 29954599, 31337820, 31627581, 1672982],
        ['exon45', 29665044, 29954858, 31338026, 31627840, 1672982]],
 't2': [['exon56', 29685988, 29975734, 31358970, 31648716, 1672982],
        ['exon49', 29676139, 29965970, 31349121, 31638952, 1672982],
        ['exon58', 29701032, 29994396, 31374014, 31667378, 1672982],
        ['exon55', 29685499, 29975341, 31358481, 31648323, 1672982],
        ['exon48', 29670028, 29959854, 31343010, 31632836, 1672982],
        ['exon15', 29548869, 29838648, 31221851, 31511630, 1672982],
        ['exon14', 29546024, 29835837, 31219006, 31508819, 1672982],
        ['exon17', 29552114, 29841969, 31225096, 31514951, 1672982],
        ['exon16', 29550463, 29840286, 31223445, 31513268, 1672982],
        ['exon11', 29528430, 29818204, 31201412, 31491186, 1672982],
        ['exon10', 29528056, 29817878, 31201038, 31490860, 1672982],
        ['exon13', 29541470, 29831304, 31214452, 31504286, 1672982],
        ['exon12', 29533259, 29823090, 31206241, 31496072, 1672982],
        ['exon37', 29652839, 29942971, 31325821, 31615953, 1672982],
        ['exon36', 29592248, 29882058, 31265230, 31555040, 1672982],
        ['exon35', 29588730, 29878576, 31261712, 31551558, 1672982],
        ['exon34', 29587388, 29877234, 31260370, 31550216, 1672982],
        ['exon19', 29554237, 29844010, 31227219, 31516992, 1672982],
        ['exon18', 29553454, 29843403, 31226436, 31516385, 1672982],
        ['exon31', 29579957, 29869719, 31252939, 31542701, 1672982],
        ['exon30', 29576003, 29865838, 31248985, 31538820, 1672982],
        ['exon5', 29496910, 29786716, 31169892, 31459698, 1672982],
        ['exon4', 29490205, 29780095, 31163187, 31453077, 1672982],
        ['exon7', 29508729, 29798504, 31181711, 31471486, 1672982],
        ['exon6', 29508441, 29798208, 31181423, 31471190, 1672982],
        ['exon1', 29421946, 29712088, 31094928, 31385070, 1672982],
        ['exon39', 29657315, 29947217, 31330297, 31620199, 1672982],
        ['exon3', 29486029, 29775812, 31159011, 31448794, 1672982],
        ['exon2', 29483002, 29772845, 31155984, 31445827, 1672982],
        ['exon54', 29684288, 29974088, 31357270, 31647070, 1672982],
        ['exon38', 29654518, 29944558, 31327500, 31617540, 1672982],
        ['exon9', 29527441, 29817314, 31200423, 31490296, 1672982],
        ['exon8', 29509527, 29799384, 31182509, 31472366, 1672982],
        ['exon42', 29663654, 29953633, 31336636, 31626615, 1672982],
        ['exon43', 29664387, 29954301, 31337369, 31627283, 1672982],
        ['exon50', 29677202, 29967037, 31350184, 31640019, 1672982],
        ['exon51', 29679276, 29969133, 31352258, 31642115, 1672982],
        ['exon53', 29683979, 29973809, 31356961, 31646791, 1672982],
        ['exon52', 29683479, 29973301, 31356461, 31646283, 1672982],
        ['exon57', 29687506, 29977422, 31360488, 31650404, 1672982],
        ['exon33', 29586051, 29875848, 31259033, 31548830, 1672982],
        ['exon32', 29585363, 29875221, 31258345, 31548203, 1672982],
        ['exon20', 29554542, 29844325, 31227524, 31517307, 1672982],
        ['exon21', 29556044, 29846184, 31229026, 31519166, 1672982],
        ['exon22', 29556854, 29846693, 31229836, 31519675, 1672982],
        ['exon23', 29557279, 29847101, 31230261, 31520083, 1672982],
        ['exon24', 29557861, 29847644, 31230843, 31520626, 1672982],
        ['exon25', 29559092, 29848908, 31232074, 31521890, 1672982],
        ['exon26', 29559719, 29849600, 31232701, 31522582, 1672982],
        ['exon27', 29560021, 29849932, 31233003, 31522914, 1672982],
        ['exon28', 29562630, 29852491, 31235612, 31525473, 1672982],
        ['exon29', 29562937, 29852740, 31235919, 31525722, 1672982],
        ['exon40', 29661857, 29951750, 31334839, 31624732, 1672982],
        ['exon41', 29663352, 29953192, 31336334, 31626174, 1672982],
        ['exon46', 29665723, 29955524, 31338705, 31628506, 1672982],
        ['exon47', 29667524, 29957364, 31340506, 31630346, 1672982],
        ['exon44', 29664838, 29954599, 31337820, 31627581, 1672982],
        ['exon45', 29665044, 29954858, 31338026, 31627840, 1672982]]}


for key, value in args.iteritems():
    if key == "exon_of_interest":
        if value is not None:
            exon_of_interest = int(value)
        else:
            exon_of_interest = "blank"
    if key == "exons_before":
        if value is not None:
            exons_before = int(value)
        else:
            exons_before = 0
    if key == "exons_after":
        if value is not None:
            exons_after = int(value)
        else:
            exons_after = 0
    if key == "gene_name":
        gene_name = value

dataframes = []
transcripts = []

if exon_of_interest != "blank":
    for key, value in results_dict.iteritems():
        transcript = key
        transcripts.append(transcript)
        headers = ["Exon number", "GrCh37_Start", "GrCh38_Start", "GrCh37_stop", "GrCh38_stop", "Positional Shift"]
        newlist = []
        exons_before_list = []
        exons_after_list = []

        for entry in value:
            exon_number = int(entry[0].strip("exon"))
            if exon_number == exon_of_interest:
                EOI = [entry]
            if exon_number > exon_of_interest:
                if exon_number <= (exon_of_interest + exons_after):
                    exons_after_list.append(entry)
            if exon_number < exon_of_interest:
                if exon_number >= (exon_of_interest - exons_before):
                    exons_before_list.append(entry)
        if len(exons_before_list) >= 1:
            if len(exons_after_list) >= 1:
                newlist = exons_before_list+EOI+exons_after_list
            else:
                newlist = exons_before_list+EOI
        else:
            newlist = EOI
        df = pandas.DataFrame(newlist, columns=headers)
        myfinisheddata = df.to_html(index=False)
        dataframes.append(myfinisheddata)

else:
    for key, value in results_dict.iteritems():
        transcript = key
        transcripts.append(transcript)
        headers = ["Exon number", "GrCh37_Start", "GrCh38_Start", "GrCh37_stop", "GrCh38_stop", "Positional Shift"]
        newlist = []
        for entry in value:
            newlist.append(entry)

        df = pandas.DataFrame(newlist, columns=headers)
        myfinisheddata = df.to_html(index=False)
        dataframes.append(myfinisheddata)



print len(dataframes)



now = datetime.datetime.now()

current_date = now.strftime("%d-%m-%Y")

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("xml_report_template.html")
# define what to pass to the template
template_vars = {"title": "Results for "+ gene_name, "transcripts": transcripts, "data": dataframes,}
# pass the template vars to the template
html_out = template.render(template_vars)
# write to a html file named of the current date
file_out = open(current_date + ".html", "w")
file_out.write(html_out.replace(
    " border=\"1\" class=\"dataframe\"", ""))
file_out.close()
