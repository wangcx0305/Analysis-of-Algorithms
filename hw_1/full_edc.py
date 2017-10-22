#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 15:00:00 2017

@author: wangchunxiao
"""

import operator
from readinput import _readinput
from edc import _edc

def _enhanceddnc(data):
    test = _readinput(data)
    
    test_xsort = sorted(test, key = operator.itemgetter(0))
    test_ysort = sorted(test, key = operator.itemgetter(1))
    
    minid, minipair = _edc(test_xsort, test_ysort)

    minipair = [(pair[0][0], pair[0][1], pair[1][0], pair[1][1]) \
                    for pair in minipair]
    sminipair = sorted(minipair, key = operator.itemgetter(0, 1, 2, 3))

    with open('output_edc.txt', 'w') as f:
       print(minid, file = f)
       for line in sminipair:
         print(line[0], line[1], line[2], line[3],  file = f)
    f.close()