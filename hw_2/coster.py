#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 13:43:47 2017

@author: wangchunxiao
"""
import pandas as pd
import io
from alignfunc import editdistance, backtrace, alignseq

with open('imp2cost.txt') as f:
    costm = pd.read_table(f, sep=',', index_col = 0, lineterminator='\n')
    
fhandle = io.open('imp2input.txt', 'rU')
file = fhandle.readlines()
fhandle.close

s = list()
t = list()
for line in file:
    seq = line.strip().split(",")
    s.append(seq[0])
    t.append(seq[1])
    
d = list()
aligns = list()
alignt = list()

     
for i in range(len(s)):
    mind, B = editdistance(s[i], t[i], costm)
    bt_ind = backtrace(B)
    seq1, seq2 = alignseq(s[i], t[i], bt_ind)
    d.append(mind)
    aligns.append(seq1)
    alignt.append(seq2)
    
with open('imp2output.txt', 'w') as f:
    for i in range(len(d)):
        print(str(aligns[i]) + "," + str(alignt[i]) + ":"+str(d[i]), file = f)
        
f.close()












     
     

