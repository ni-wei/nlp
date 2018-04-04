in_file = open("txt_temp.txt")	# input file. All sentences are Calcium-relevant. Manually extracted from the original training.txt.
output = open("test.txt", "w+")	# output file.
output0 = open("testB.txt", "w+")	# output file.

with in_file as f:
	for line in f:
		if line[len(line)-2] == '0':
			output0.write(line)
		else:
			output.write(line)

in_file.close()
output.close()
output0.close()


