#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 17:17:34 2017

@author: wangchunxiao
"""
import operator
from brute import _brute
from dist import _dist

def _dnc(points):
    n = len(points)
    if n <= 4:
        return _brute(points)
    divider = points[int(n / 2.0)]
    points_left = [point for point in points if point[0] < divider[0]]
    points_right = [point for point in points if point[0] >= divider[0]]
    lminid, lminipair = _dnc(points_left)
    rminid, rminipair = _dnc(points_right)
    if lminid < rminid:
       minid = lminid
       minipair = lminipair
    elif lminid == rminid:
       minid = lminid
       minipair = lminipair + rminipair
    else:
       minid = rminid
       minipair = rminipair
    points_closed = [point for point in points \
                      if abs(point[0] - divider[0]) <= minid]
    points_closed = sorted(points_closed, key = operator.itemgetter(1))
    nc = len(points_closed)
    if nc > 1:
        temp = min( [_dist(points_closed[i], points_closed[j])
                     for i in range(nc - 1)
                     for j in range(i + 1, nc)])
        if temp < minid:
             minid = temp
             minipair = [sorted([points_closed[i], points_closed[j]])
                           for i in range(n - 1)
                           for j in range(i + 1, nc)
                           if _dist(points_closed[i], points_closed[j]) == minid]  
        if temp == minid:
              temppair = [sorted([points_closed[i], points_closed[j]]) 
                           for i in range(n - 1)
                           for j in range(i + 1, nc)
                           if _dist(points_closed[i], points_closed[j]) == minid]
              temp = [pair for pair in temppair if pair not in minipair]
              minipair = minipair + temp                      
    return minid, minipair
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    