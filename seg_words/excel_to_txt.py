'''
This file is used to extract information that we are interesed in from reports sent by hospitals.
There are two main jobs that this file does. The first one is rearranging the image findings into txt
files which are named by patient combined with the data when patient take the inspection. However,
the second job is to build raw annotation files corresponding with every txt file.
'''

import pandas as pd
import re
from os import listdir
from os.path import isfile, join

'''
We build a dictionary to store information for each patient, which means that
we need to initialize this dictionary in every iteration. Hence, we construct a
helper function to finish this job.
'''
def ini_variables(variables):
    # The ini in the function's name is the abbre of initialize. this function
    # initialize the value to an empty string for every key in objective dictionary.

    #variables: dictionary type
    #return: dictionary
    for item in variables:
        variables[item] = ''
    return variables



'''We have some key word that will indicate whether we do need a sentence or not.
We store the whole hot words into a list. This function will iterate the hot word
list and check if the current word is in the current sentence. We will reture Ture
as soon as any word in our hot word list is found in the current sentence, otherwise,
we will return False when all word in hot word list have been checked.
'''
def check_string_exist_in_lookup_table(lookup_table, string):
    #lookup_table: list     the hot word list where you put the information that you care about.
    #return: Boolean
    for item in lookup_table:
        if item in string:
            return True
    return False




'''We build a function which will be helpful when we want to get the coordinates
of specific substring from a string. If the substring we provide is in the original
string, function will provide the information of the coordinates for both starting
and ending point. otherwise, function will assign -1 to these two coordinates.
'''
def find_the_location_of_substring(string, substring):
    #substring: str
    #string: str
    #return: list   the first element is the list is the starting point while the
    #               second one is the ending point.
    if substring and substring != 'unknown':
        start = string.find(substring)
        end = start+len(substring)
    else:
        start = -1
        end = -1
    return [start, end]






'''You need to fill this code seciton manually'''
mypath = 'iter_input/' #the file path that you want to process
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#print (onlyfiles) #'test_Corony.xlsx'
pre_path = '' #the path that you store the summary file for each patient. for example '/home/peter/Desktop/Corony_2017_7-12_1_2099/'
nn_path = '' #the path that you store the ann files, also a directory. for example '/home/peter/Desktop/Corony_2017_7-12_1_annotation/'
path_text_data_name = '' #the path that you need to store the txt files in server (using Brat) also a directory for example '/home/peter/Desktop/temp/'










#Read excel file into dataframe using pandas
#df = pd.read_excel(file_name)
#Setting a path that keep the txt summary files.
pre_path = pre_path

#We inspect the orginal data and find some patterns in there. Hence we build three key words lists that will
#help us to determine which category the current paragraph should be assigned to.
lookup_table_sec_calcium_score = ['平扫钙化积分', '钙化积分', '平扫', '扫钙化积分']
lookup_table_sec_rebuild = ['VR', 'CRP', 'MIP',  '旋支', '右冠状', '右主干', '左主干', '左冠', '降支', 'LM', 'CX', 'RCA']
lookup_table_sec_mpr = ['MPR', 'MRP', '心包', '心壁', '瓣', '心房', '心室']


file_path = 'report_in_txt.txt'
with open(file_path, 'w+') as f:
	#Iterate every row/item in the original excel files. Each row/item records the infomation of 1 patient.
	for file_name in onlyfiles:
		df = pd.read_excel(join(mypath, file_name))
		for index, row in df.iterrows():
			#Defines and initialize some variables that will be used to store the information that we are interesed in.
			global_overall_findings = ''
			calcium_score_overall_findings = ''
			VR_overall_findings = ''
			MPR_overall_findings = ''
			opening_info = ''
			dominant_system_info = ''
			LCA_info = ''
			LAD_info = ''
			LCX_info = ''
			RCA_info = ''
			calcium_volume = ''
			calcium_mass = ''
			calcium_score = ''
			heart_size_info = ''
			heart_wall_info = ''
			pericardium_info = ''
			pleura_info = ''
			valve_info = ''
			impression_info = ''
			other_info = ''
			#Because it is possible that the excel file consist two rows which come from a same patient. Hence, we combine
			#the information of the data when the examination is done with the patient ID as the files' name.
			exam_date = row[1][4:12]
			#construct summary files for each patient as .txt files.
			#  file_path = pre_path + row[0] + '_' + exam_date + '.txt'
			#fetch the image findings
			performance = row['影像学表现']
			# only handle items that are str objects. We do this because for some patient, the image findings filed are missing
			# and if this issue happens, we will get a Nan data. we do not consider patients whose image findings are missing.
			# Notice that Nan data is explained as float data by python compiler.
			if isinstance(performance, str):






				#Store data from memory to disk
				# f.write(global_overall_findings)
				f.write(performance+'\n')
				##f.write('影像学表现\n')

			impression_info = row['影像学诊断']
			# only print impression_info if they are str objects
			if isinstance(impression_info, str):
				##f.write('影像学诊断\n')
				f.write(impression_info+'\n')
				# f.write('\n\n\n\n\n\n')


