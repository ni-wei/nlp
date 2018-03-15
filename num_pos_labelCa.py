import re
in_file = open("calcium.txt")
output = open("RL_Ca.txt", "w+")
#str_mass = '钙化质量为'  # calcium mass. What we are interested in.
with in_file as f:
	for line in f:
		m_volume = re.search(r"钙化容积(约)?(为)?(立方毫米)?[-+ ]?(\d*\.\d+|\d+)*", line)
		if m_volume:
			#output.write('calcium_volume' + '\t' + m_volume.group(0)) + '\n')
			volume_substr = m_volume.group(0)
			volume_num = re.search(r"([-+ ]|\d*\.\d+|\d+)+", volume_substr).group(0)  # in the volume_substr substring, find the number/space (assuming there is only 1 number/space).
			output.write('calcium_volume' + '\t' + line.rstrip('\n') + '\t' + str(m_volume.end()-len(volume_num)) + '\t' + str(m_volume.end()) + '\n') ##+ '\t' + volume_num

	## below is the latest working version for calcium mass
	# if '钙化质量(约)?(为)?(毫克)?[-+ ]?(\d*\.\d+|\d+)*' exists in this line, find the calcium mass number.
		m_mass = re.search(r"(钙化|等效)质量(约)?(为)?(毫克)?[-+ ]?(\d*\.\d+|\d+)*", line)
		if m_mass:
			mass_substr = m_mass.group(0)
			mass_num = re.search(r"([-+ ]|\d*\.\d+|\d+)+", mass_substr).group(0)  # in the mass_substr substring, find the number/space (assuming there is only 1 number/space).
			output.write('calcium_mass' + '\t' + line.rstrip('\n') + '\t' + str(m_mass.end()-len(mass_num)) + '\t' + str(m_mass.end()) + '\n') ##+ '\t' + mass_num


	# if '钙化质量(约)?(为)?(毫克)?[-+ ]?(\d*\.\d+|\d+)*' exists in this line, find the calcium score number.
		m_score = re.search(r"[^平扫]钙化积分(约)?(为)?[-+ \n]?(\d*\.\d+|\d+)*", line)
		if m_score:
			score_substr = m_score.group(0)
			score_num = re.search(r"([-+ \n]|\d*\.\d+|\d+)+", score_substr).group(0)  # in the score_substr substring, find the number/space (assuming there is only 1 number/space).
			output.write('calcium_score' + '\t' + line.rstrip('\n') + '\t' + str(m_score.end()-len(score_num)) + '\t' + str(m_score.end()) + '\n') ##+ '\t' + score_num

in_file.close()
output.close()


