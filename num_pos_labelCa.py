import re
in_file = open("calcium.txt")	# input file. All sentences are Calcium-relevant. Manually extracted from the original training.txt.
output = open("RL_Ca.txt", "w+")	# output file.

with in_file as f:
	for line in f:
	## for calcium volume
	## if '钙化容积(约)?(为)?(立方毫米)?[-+ ]?(\d*\.\d+|\d+)*' exists in this line, find the calcium volume number.
		m_volume = re.search(r"钙化容积(约)?(为)?(立方毫米)?[-+ ]?(\d*\.\d+|\d+)*", line)	# m_volume is the match object returned by RE search, using the specific RE pattern.
		if m_volume:
			volume_substr = m_volume.group(0)	# if pattern found, m_volume.group(0) returns the entire match.
			volume_num = re.search(r"([-+ ]|\d*\.\d+|\d+)+", volume_substr).group(0)	# in the volume_substr substring (the match), find the number or a space + the number (assuming there is only 1 number/space) using RE search.
			output.write('calcium_volume' + '\t' + line.rstrip('\n') + '\t' + str(m_volume.end()-len(volume_num)) + '\t' + str(m_volume.end()) + '\n') ##+ '\t' + volume_num	# output: label + tab + orig. line + tab + start pos. of num. + tab + end pos. of num. (also the end position of the m_volume string).

	## for calcium mass
	## if '(钙化|等效)质量(约)?(为)?(毫克)?[-+ ]?(\d*\.\d+|\d+)*' exists in this line, find the calcium mass number.
		m_mass = re.search(r"(钙化|等效)质量(约)?(为)?(毫克)?[-+ ]?(\d*\.\d+|\d+)*", line)	# m_mass is the match object returned by RE search, using the specific RE pattern.
		if m_mass:
			mass_substr = m_mass.group(0)	# if pattern found, m_mass.group(0) returns the entire match.
			mass_num = re.search(r"([-+ ]|\d*\.\d+|\d+)+", mass_substr).group(0)  # in the mass_substr substring (the match), find the number or a space + the number (assuming there is only 1 number/space) using RE search.
			output.write('calcium_mass' + '\t' + line.rstrip('\n') + '\t' + str(m_mass.end()-len(mass_num)) + '\t' + str(m_mass.end()) + '\n') ##+ '\t' + mass_num	# output: label + tab + orig. line + tab + start pos. of num. + tab + end pos. of num. (also the end position of the m_mass string).

	## for calcium score
	## if '[^平扫]钙化积分(约)?(为)?[-+ \n]?(\d*\.\d+|\d+)*' exists in this line, find the calcium score number.
		m_score = re.search(r"[^平扫]钙化积分(约)?(为)?[-+ \n]?(\d*\.\d+|\d+)*", line)	# m_score is the match object returned by RE search, using the specific RE pattern.
		if m_score:
			score_substr = m_score.group(0)	# if pattern found, m_score.group(0) returns the entire match.
			score_num = re.search(r"([-+ \n]|\d*\.\d+|\d+)+", score_substr).group(0)  # in the score_substr substring (the match), find the number or a space + the number (assuming there is only 1 number/space) using RE search.
			output.write('calcium_score' + '\t' + line.rstrip('\n') + '\t' + str(m_score.end()-len(score_num)) + '\t' + str(m_score.end()) + '\n') ##+ '\t' + score_num	# output: label + tab + orig. line + tab + start pos. of num. + tab + end pos. of num. (also the end position of the m_score string).

in_file.close()
output.close()


