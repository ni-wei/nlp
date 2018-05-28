import re
in_file = open("../word_seg/dataFromNing_backup/eighty_reports.txt")	# input file. All sentences are Calcium-relevant. Manually extracted from the original training.txt.
output = open("CaScore.txt", "w+")	# output file.

with in_file as f:
	for line in f:
	## for calcium score
	## if '[^平扫]钙化积分(约)?(为)?[-+ \n]?(\d*\.\d+|\d+)*' exists in this line, find the calcium score number.
		m_score = re.search(r"[^平扫]钙化积分(约)?(为)?(,)?[-+ \n]?(\d*\.\d+|\d+)*", line)	# m_score is the match object returned by RE search, using the specific RE pattern.
		if m_score:
			score_substr = m_score.group(0)	# if pattern found, m_score.group(0) returns the entire match.
			try:
			    score_num = re.search(r"([-+ \n]|\d*\.\d+|\d+)+", score_substr).group(0)  # in the score_substr substring (the match), find the number or a space + the number (assuming there is only 1 number/space) using RE search.
			except:
			    score_num = 'null score'
			output.write(score_num + '\n') ##+ '\t' + score_num	# output: label + tab + orig. line + tab + start pos. of num. + tab + end pos. of num. (also the end position of the m_score string).

in_file.close()
output.close()


