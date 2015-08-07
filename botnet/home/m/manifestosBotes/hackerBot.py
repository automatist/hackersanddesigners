import sys
import os
from random import choice
import random
import re
import time

#import nltk
# infinite loop that keeps reading & responding
#while True:
#    zin = sys.stdin.readline()
#    if not zin:
#        break
# do something to form zin to out
#txt = 'MetaheavenManifesto.txt'


txt = 'MetaheavenManifesto.txt'


def sentences(txt):
	txt = ''.join(open(txt).readlines())
	basket = re.split(r' *[\.\?!][\'"\)\]]* *', txt)
	sentence = random.choice(basket)
	replaced = sentence.replace("designer" , "hacker").replace("design", "hack").replace("desiners", "hackers").replace("Designers" , "Hackers").replace("designing" , "hacking")
	tokens = ' '.join(replaced.replace('\n', '') +".")
	return tokens
	if tokens == '.':
		tokens = ' '.join(replaced.replace('.', '') )
		print 
		"""
 :::=======  :::====  :::= === ::: :::===== :::===== :::===  :::==== :::==== 
 ::: === === :::  === :::===== ::: :::      :::      :::     :::==== :::  ===
 === === === ======== ======== === ======   ======    =====    ===   ===  ===
 ===     === ===  === === ==== === ===      ===          ===   ===   ===  ===
 ===     === ===  === ===  === === ===      ======== ======    ===    ====== 
""" 

while True:
	replaced = sentences(txt)
	tstr = time.strftime("%H:%M:%S", time.localtime())
	out = u"({0}) {1}".format(tstr, "_HackerBot")
	sys.stdout.write(out.encode("utf-8")+"\n")
	sys.stdout.flush()
	# change a sentence every 5 sec
	time.sleep(10)
	print replaced
   


			

		

                
	


		
		

#format = on_pubmsg(replaced)
#print format
#print type(sentance)
#print sentance
