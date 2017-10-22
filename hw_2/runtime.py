#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 22:45:48 2017

@author: wangchunxiao
"""

import time
import numpy as np
import pandas as pd
import io
from alignfunc import editdistance, backtrace, alignseq
from matplotlib import pyplot as plt

with open('imp2cost.txt') as f:
    costm = pd.read_table(f, sep=',', index_col = 0, lineterminator='\n')
    
fhandle = io.open('imp2input.txt', 'rU')
file = fhandle.readlines()
fhandle.close


####500 sequence####
t_500 = list()

for i in range(10):
 seq1 = np.random.choice(['A', 'G', 'T', 'C'], 500)
 seq1 = "".join(seq1)
 seq2 = np.random.choice(['A', 'G', 'T', 'C'], 500)
 seq2 = "".join(seq2)
 start = time.time()
 d, B = editdistance(seq1, seq2, costm)
 bt_ind = backtrace(B)
 w1, w2 = alignseq(seq1, seq2, bt_ind)
 t_500.append(time.time() - start)
 
np.mean(t_500) ##5.2957

t_1000 = list()

for i in range(10):
 seq1 = np.random.choice(['A', 'G', 'T', 'C'], 1000)
 seq1 = "".join(seq1)
 seq2 = np.random.choice(['A', 'G', 'T', 'C'], 1000)
 seq2 = "".join(seq2)
 start = time.time()
 d, B = editdistance(seq1, seq2, costm)
 bt_ind = backtrace(B)
 w1, w2 = alignseq(seq1, seq2, bt_ind)
 t_1000.append(time.time() - start)

np.mean(t_1000) ##20.9122


t_2000 = list()

for i in range(10):
 seq1 = np.random.choice(['A', 'G', 'T', 'C'], 2000)
 seq1 = "".join(seq1)
 seq2 = np.random.choice(['A', 'G', 'T', 'C'], 2000)
 seq2 = "".join(seq2)
 start = time.time()
 d, B = editdistance(seq1, seq2, costm)
 bt_ind = backtrace(B)
 w1, w2 = alignseq(seq1, seq2, bt_ind)
 t_2000.append(time.time() - start)
 
np.mean(t_2000) ##82.5379


t_4000 = list()

for i in range(10):
 seq1 = np.random.choice(['A', 'G', 'T', 'C'], 4000)
 seq1 = "".join(seq1)
 seq2 = np.random.choice(['A', 'G', 'T', 'C'], 4000)
 seq2 = "".join(seq2)
 start = time.time()
 d, B = editdistance(seq1, seq2, costm)
 bt_ind = backtrace(B)
 w1, w2 = alignseq(seq1, seq2, bt_ind)
 t_4000.append(time.time() - start)
 
np.mean(t_4000)###332.9839


t_5000 = list()

for i in range(10):
 seq1 = np.random.choice(['A', 'G', 'T', 'C'], 5000)
 seq1 = "".join(seq1)
 seq2 = np.random.choice(['A', 'G', 'T', 'C'], 5000)
 seq2 = "".join(seq2)
 start = time.time()
 d, B = editdistance(seq1, seq2, costm)
 bt_ind = backtrace(B)
 w1, w2 = alignseq(seq1, seq2, bt_ind)
 t_5000.append(time.time() - start)
 
np.mean(t_5000)###533.5867


x = (500, 1000, 2000, 4000, 5000)
y = (5.2957, 20.9122, 82.5379, 332.9839, 533.5867)

logx = np.log(x)
logy = np.log(y)

plt.plot(x, y)
plt.xlabel('sequence length')
plt.ylabel('empirical time')
plt.title('time vs length')

plt.plot(logx, logy)
plt.xlabel('log of sequence length')
plt.ylabel('log of empirical time')
plt.title('log-log time vs length')



