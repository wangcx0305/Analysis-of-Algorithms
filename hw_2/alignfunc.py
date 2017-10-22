#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 22:49:39 2017

@author: wangchunxiao
"""

import numpy as np

def editdistance(seq1, seq2, costm):
     m = len(seq1) + 1
     n = len(seq2) + 1
     D = np.zeros((m, n), dtype = np.int)
     for i in range(1, m):
         D[i, 0] = D[i - 1, 0] + costm.get_value(seq1[i - 1], "-")
     for j in range(1, n):
         D[0, j] = D[0, j - 1] + costm.get_value("-", seq2[j - 1]) 
     B = np.zeros((m, n), dtype = [("del", 'b'), ("sub",'b'),("ins", 'b')])
     B[1:, 0] = (1, 0, 0)
     B[0, 1:] = (0, 0, 1)
     for i, l1 in enumerate(seq1, start = 1):
         for j, l2 in enumerate(seq2, start = 1):
             dele = D[i - 1, j] + costm.get_value(seq1[i - 1], "-")
             ins = D[i, j - 1] + costm.get_value("-", seq2[j - 1])
             subs = D[i - 1, j - 1] + costm.get_value(seq1[i - 1], seq2[j - 1])
             mind = np.min([dele, ins, subs])
             B[i, j] = (dele == mind, subs == mind, ins == mind)
             D[i, j] = mind
     return D[m - 1, n - 1], B

     
def backtrace(B):
    i = B.shape[0] - 1
    j = B.shape[1] - 1
    backtrace_ind = [(i, j)]

    while (i, j) != (0, 0):
        if B[i, j][0]:
            i, j = i - 1, j
        elif B[i, j][2]:
            i, j = i, j - 1
        else:
            i, j = i - 1, j - 1    
        backtrace_ind.append((i, j))
        
    return backtrace_ind

def alignseq(seq1, seq2, bt_ind):
     alignseq1 = []
     alignseq2 = []
     backtrace = bt_ind[::-1]
     for k in range(len(backtrace) - 1):
         i_0, j_0 = backtrace[k]
         i_1, j_1 = backtrace[k + 1]
         w1 = None
         w2 = None
         if i_0 < i_1 and j_0 < j_1:
                w1 = seq1[i_0]
                w2 = seq2[j_0]
         elif j_0 == j_1:
                w1 = seq1[i_0]
                w2 = "-"
         else:
                w1 = "-"
                w2 = seq2[j_0]
         alignseq1.append(w1)
         alignseq2.append(w2)
     
     return "".join(alignseq1), "".join(alignseq2)
