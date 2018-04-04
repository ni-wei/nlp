import jieba
# import jieba.posseg as pseg
import re
from operator import itemgetter, attrgetter, methodcaller
import time
from collections import Counter

##jieba.enable_parallel(4) # 开启并行分词模式，参数为并发执行的进程数

##content = open('report_in_txt.txt', 'rb').read()  # GuiZhou reports as the input. both finding and diagnosis. 
##content = open('input_brain5.txt', 'rb').read()

start_time = time.time()
##jieba.load_userdict("coronary_dict.txt")
##words = jieba.lcut(content)  # words = pseg.lcut(content)  ## 默认是精确模式
##words = [x for x in jieba.cut(content)] # if len(x) >= 2]

#words = [x for x in open('jiebaCutOutput.txt', 'r').readlines()] # if len(x) >= 2]

words = [x for x in open('jiebaCutOutput.txt', 'r').read()] # if len(x) >= 2]
##words_set = set(words)
elapsed_time = time.time() - start_time
time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
print(elapsed_time)
##jieba.disable_parallel() # 关闭并行分词模式
#

## delete each line that contains a number. #To-do: refine it. better speed it up.
for index, word in enumerate(words):
	m_number = re.search(r"(\d*\.\d+|\d+)+", word)
	if m_number: ##is None:
		del(words[index]) ## print (word.word, word.flag)
c = Counter(words)

output = open("buffer_read.txt", "w+")	# output file.

with output as f:
	for word, count in c.most_common():
		f.write(word+' '+str(count)+'\n')

output.close()

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

