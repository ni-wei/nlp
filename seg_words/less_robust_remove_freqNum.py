## less robust because we assume the input file is perfectly formatted as 'str1 \space str2 \n'.
## we split the input file line by line, and print only str1 into the output file.
## if it reports error, it is probably due to that there is an empty line in the input file.

in_file = open("new_dict.txt")	# input file. 
output = open("word_only.txt", "w+")	# output file.

with in_file as f:
	for line in f:
		result_split = line.split()
		output.write(result_split[0]+'\n')

in_file.close()
output.close()


