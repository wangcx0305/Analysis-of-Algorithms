#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 16:59:32 2017

@author: wangchunxiao
"""

import io

def _readinput(data):
    fhandle = io.open(data, 'rU')
    file = fhandle.readlines()
    fhandle.close()
    test = list()
    
    for i in range(0, len(file)):
       test.append(file[i].strip().split())
       test[i][0] = float(test[i][0])
       test[i][1] = float(test[i][1])
       
    return test