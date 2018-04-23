import jieba
# import jieba.posseg as pseg
import re
from operator import itemgetter, attrgetter, methodcaller
import time
from collections import Counter

##jieba.enable_parallel(4) # 开启并行分词模式，参数为并发执行的进程数

content = open('report_in_txt.txt', 'rb').read()  # GuiZhou reports as the input. both finding and diagnosis. 
##content = open('input_brain5.txt', 'rb').read()

start_time = time.time()
jieba.load_userdict("GuiZhou_dict_sorted_v0.txt")
##words = jieba.lcut(content)  # words = pseg.lcut(content)  ## 默认是精确模式
words = [x for x in jieba.cut(content)] # if len(x) >= 2]

elapsed_time = time.time() - start_time
time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
print(elapsed_time)
##jieba.disable_parallel() # 关闭并行分词模式
#
# 将结果存入文件jiebaCutOutput.txt中,
# 相当于做一个缓存
##with open('jiebaOutput.txt','w+') as f: #'jiebaCutOutput.txt'
##	for word in words:
##		f.write(word+'\n')

## delete each line that contains a number. #To-do: refine it. better speed it up.
##for index, word in enumerate(words):
	##m_number = re.search(r"(\d*\.\d+|\d+)+", word)
	##if m_number: ##is None:
		##del(words[index]) ## print (word.word, word.flag)
c = Counter(words)


# words_sort = sorted(words, key=attrgetter('flag'))
# words_set = sorted(set(words), key=attrgetter('flag'))
##words_set = set(words)

##comparison: with or without user dict.
##words_default = jieba.lcut(content)  # 默认是精确模式
##jieba.load_userdict("coronary_dict.txt")
##words_w_user_dict = jieba.lcut(content)
##words_set = {x for x in set(words_w_user_dict) if x not in set(words_default)}
##words_set = {x for x in set(words_default) if x not in set(words_w_user_dict)}
##End of comparison: with or without user dict.

##ToDo: add "with open('xxx.txt','w+') as f:" to automatize the writing process.
##for word in words_set:# in words_all:
	##m_number = re.search(r"(\d*\.\d+|\d+)+", word)
	##if m_number is None:
		##print (word) ## print (word.word, word.flag)
with open('test_dict.txt','w+') as f: #'new_dict.txt'
	##for word in words_set:
		##if check_str_number(word) is '<num>':
			##m_number = re.search(r"(\d*\.\d+|\d+)+", word)
			##if m_number is None:
				##f.write(word+'\n')
	for word, count in c.most_common():
		m_number = re.search(r"(\d*\.\d+|\d+)+", word)
		if m_number is None:
			f.write(word+' '+str(count)+'\n')
