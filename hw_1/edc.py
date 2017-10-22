#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 17:35:59 2017

@author: wangchunxiao
"""

from brute import _brute
from dist import _dist

def _edc(points_xsort, points_ysort):  
    n = len(points_xsort)
    if n <= 4:
        return _brute(points_xsort)
    divider = points_xsort[int(n / 2.0)]
    points_xleft = [point for point in points_xsort if point[0] < divider[0]]
    points_xright = [point for point in points_xsort if point[0] >= divider[0]]
    points_yleft = [point for point in points_ysort if point[0] < divider[0]]
    points_yright = [point for point in points_ysort if point[0] >= divider[0]]
    lminid, lminipair = _edc(points_xleft, points_yleft)
    rminid, rminipair = _edc(points_xright, points_yright)
    if lminid < rminid:
       minid = lminid
       minipair = lminipair
    elif lminid == rminid:
       minid = lminid
       minipair = lminipair + rminipair
    else:
       minid = rminid
       minipair = rminipair
    points_closed = [point for point in points_ysort \
                      if abs(point[0] - divider[0]) <= minid]
    nc = len(points_closed)
    if nc > 1:
        temp = min( [_dist(points_closed[i], points_closed[j])
                     for i in range(nc - 1)
                     for j in range(i + 1, min(i + 8, nc))])
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
    

    
    
