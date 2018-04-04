import jieba
# import jieba.posseg as pseg
import re
from operator import itemgetter, attrgetter, methodcaller
import time

jieba.enable_parallel(4) # 开启并行分词模式，参数为并发执行的进程数

content = open('iter.txt', 'rb').read()  # GuiZhou reports as the input. both finding and diagnosis. 

start_time = time.time()
jieba.load_userdict("coronary_dict.txt")
words = jieba.lcut(content)  # words = pseg.lcut(content)  ## 默认是精确模式

elapsed_time = time.time() - start_time
time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
print(elapsed_time)
jieba.disable_parallel() # 关闭并行分词模式


# words_sort = sorted(words, key=attrgetter('flag'))
# words_set = sorted(set(words), key=attrgetter('flag'))
words_set = set(words)
for word in words_set:# in words_all:
	m_number = re.search(r"(\d*\.\d+|\d+)+", word)
	if m_number is None:
		print (word)
		# print (word.word, word.flag)

