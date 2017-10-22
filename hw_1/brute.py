#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 16:30:45 2017

@author: wangchunxiao
"""
from dist import _dist 

def _brute(test):
        
    n = len(test)
    
    if n < 2:
        minid = float('inf')
        minipair = [[None, None]]
    else:
        minid = min([_dist(test[i], test[j])
                       for i in range(n - 1)
                       for j in range(i + 1, n)])
        minipair = [sorted([test[i], test[j]])
                     for i in range(n - 1)
                     for j in range(i + 1, n)
                     if _dist(test[i], test[j]) == minid]        
    return minid, minipair
