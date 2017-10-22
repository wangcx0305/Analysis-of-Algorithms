#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 14:48:39 2017

@author: wangchunxiao
"""
from dnc import _dnc
from readinput import _readinput
import operator

def _divideandconquer(data):
    test = _readinput(data)
    test_xsort = sorted(test, key = operator.itemgetter(0))
    minid, minipair = _dnc(test_xsort)
    minipair = [(pair[0][0], pair[0][1], pair[1][0], pair[1][1]) \
                    for pair in minipair]
    sminipair = sorted(minipair, key = operator.itemgetter(0, 1, 2, 3))
    
    with open('output_dc.txt', 'w') as f:
       print(minid, file = f)
       for line in sminipair:
        print(line[0], line[1], line[2], line[3],  file = f)
    f.close()
    