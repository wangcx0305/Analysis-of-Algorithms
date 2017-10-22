#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 14:57:18 2017

@author: wangchunxiao
"""

import operator
from readinput import _readinput
from brute import _brute

def _bruteforce(data):
    test = _readinput(data)
    
    minid, minipair = _brute(test)
    
    minipair = [(pair[0][0], pair[0][1], pair[1][0], pair[1][1]) \
                 for pair in minipair]
    sminipair = sorted(minipair, key = operator.itemgetter(0, 1, 2, 3))
    
    with open('output_bf.txt', 'w') as f:
        print(minid, file = f)
        for line in sminipair:
          print(line[0], line[1], line[2], line[3],  file = f)
    f.close()