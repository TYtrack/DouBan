
import jieba
f = open('douban.txt', 'r',encoding='utf-8')



import pandas as pd
import jieba.analyse
import jieba
import jieba.posseg
import os, sys


def input(trainname):
    traindata = []
    with open(trainname, 'rb') as f:
        line = f.readline()
        count = 0
        while line:
            try:
                traindata.append(line)
                count += 1
            except:
                print ("error:", line, count)
            line=f.readline()
    return traindata


filepath = 'douban.txt'
QueryList = input(filepath)

writepath = 'writefile.txt'
csvfile = open(writepath, 'w')

POS = {}
for i in range(len(QueryList)):
    if i%2==0:
        continue
    s = []
    str = ""
    words = jieba.posseg.cut(QueryList[i])
    #只保留n,v,j
    
    allowPOS = ['n','v','j']
    for word, flag in words:
        POS[flag]=POS.get(flag,0)+1
        #词的长度>1
        if (flag[0] in allowPOS) and len(word)>=2:
            str += word + " "
    #print(str)
    #保存
    csvfile.write("".join('%s' %id for id in str)+'\n')
csvfile.close()
print (POS)
