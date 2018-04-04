import re
in_file = open("calcium.txt")	# input file. All sentences are Calcium-relevant. Manually extracted from the original training.txt.
output = open("RL_Ca.txt", "w+")	# output file.

with in_file as f:
	for line in f:
	## for calcium volume
	## if '钙化容积(约)?(为)?(立方毫米)?[-+ ]?(\d*\.\d+|\d+)*' exists in this line, find the calcium volume number.
		m_volume = ['钙化容积', '钙化容积为', '钙化容积为立方毫米'] #re.search(r"钙化容积(约)?(为)?(立方毫米)?[-+ ]?(\d*\.\d+|\d+)*", line)	# 
		if any(x in line for x in m_volume):
			output.write('calcium_volume' + '\t' + line.rstrip('\n') + '\n')
		#else:
			#output.write ("nothing about calcium volume is found in this line" + '\n')

### To-do/problem foreseen: after using the 'any' function to find the desired pattern, how shall i localize the number?
### One possible method is "if (line.find('钙化容积') != -1) and (line.find('钙化容积为') != -1) and ...", but it seems tedious.
### Also not sure whether this method is correct algorithm-wise. Thus I stop here.
in_file.close()
output.close()

