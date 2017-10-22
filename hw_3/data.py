#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 14:11:33 2017

@author: wangchunxiao
"""

import io

fhandle = io.open('Corvallis.csv', 'rU')
file = fhandle.readlines()[1:]
fhandle.close

temp = list()
day = list()

for line in file:
    seq = line.strip().split(';')
    temp.append(float(seq[7]))
    day.append(int(seq[8]))

with open('temp.csv', 'w') as f:
    for data in temp:
        print(data, file = f)
f.close()

with open('day.csv', 'w') as f:
    for data in day:
        print(data, file = f)
f.close()