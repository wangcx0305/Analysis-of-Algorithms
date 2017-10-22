#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 12:27:17 2017

@author: wangchunxiao
"""

from matplotlib import pyplot as plt 

time_bf = [0.01943, 1.601, 158.23, 12000]
time_dnc = [0.003285, 0.0644, 1.23, 24.84]
time_edc = [0.003678, 0.0578, 1.11, 19.46]


x = [100, 1000, 10000, 100000]
plt.subplot(1, 2, 1)
plt.plot(x, time_bf)
plt.xlabel('input size')
plt.ylabel('running time')
plt.title('brute force')

plt.subplot(1, 2, 2)
plt.plot(x, time_dnc)
plt.plot(x, time_edc)
plt.xlabel('input size')
plt.ylim(-1, 25)
plt.ylabel('running time')
plt.legend(['naive dnc', 'enhanced dnc'], loc = 'upper left')

plt.subplot(1, 3, 3)
plt.plot(x, time_edc)
plt.xlabel('input size')
plt.ylim(-1, 20)
plt.ylabel('running time')
plt.title('enhanced dnc')
