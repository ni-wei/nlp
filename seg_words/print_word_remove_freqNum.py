##ToDo: a more robust version. 
##Unsolved: if the format of a certain line is ' 2976162' or '  1803250', then the output print is the number. That is not what we want.
##However, the unsolved problem is trivial for the current input file "new_dict.txt".
##We can either ignore the wrong output prints, or simply delete those "problematic" input lines beforehand.
import sys
## print(sys.argv[1:])
in_file = open(sys.argv[1])	# input file.
output = open(sys.argv[2], "w+")	# output file.

with in_file as f:
	for line in f:
		#output.write(line[:len(line)-1])
		result_split = line.split()
		count = 0
		for element in result_split:
			count+=1
			if count % 2 == 1: #this is the remainder operator
				output.write(element + '\n')

in_file.close()
output.close()


