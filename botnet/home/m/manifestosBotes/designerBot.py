import sys
import os
from random import choice
import random 
import time
import re

################### designerBot

txt = 'HackerManifesto.txt'
counter = 0
def sentences(txt):
    txt = ''.join(open(txt).readlines())
    basket = re.split(r' *[\.\?!][\'"\)\]]* *', txt)
    sentence = random.choice(basket)
    replaced = sentence.replace("hacker" , "designer").replace("hack", "design").replace("hackers", "desiners").replace("Hackers" , "Designers").replace("hacking" , "designing")
    tokens = ''.join(replaced.replace('\n', '') + ".")
    return tokens
    #line = tokens.rstrip().decode("utf-8")
    if tokens == '.':
        tokens = ''.join(replaced.replace('\n', ''))
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
    out = u"({0}) {1}".format(tstr, "_DesignerBot")
    sys.stdout.write(out.encode("utf-8")+"\n")
    sys.stdout.flush()
    # change sentence in every 5sec
    time.sleep(5)
    print replaced    		

