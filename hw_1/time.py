#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 14:01:32 2017

@author: wangchunxiao
"""

from inputgenerate import _inputgenerate
from full_bf import _bruteforce
from full_dnc import _divideandconquer
from full_edc import _enhanceddnc
import numpy as np
import time

time_102_bf = list()
time_102_dnc = list()
time_102_edc = list()

for i in range(0, 10):
   self_input = _inputgenerate(100)
   start = time.time()
   _bruteforce('self_example.input')
   t = time.time() - start
   time_102_bf.append(t)
   start = time.time()
   _divideandconquer('self_example.input')
   t = time.time() - start
   time_102_dnc.append(t)
   start = time.time()
   _enhanceddnc('self_example.input')
   t = time.time() - start
   time_102_edc.append(t)
   
mean_102_bf = np.mean(time_102_bf)#0.01943
mean_102_dnc = np.mean(time_102_dnc)#0.003285
mean_102_edc = np.mean(time_102_edc)#0.003678


time_103_bf = list()
time_103_dnc = list()
time_103_edc = list()

for i in range(0, 10):
   self_input = _inputgenerate(1000)
   start = time.time()
   _bruteforce('self_example.input')
   t = time.time() - start
   time_103_bf.append(t)
   start = time.time()
   _divideandconquer('self_example.input')
   t = time.time() - start
   time_103_dnc.append(t)
   start = time.time()
   _enhanceddnc('self_example.input')
   t = time.time() - start
   time_103_edc.append(t)
   
mean_103_bf = np.mean(time_103_bf)#1.601
mean_103_dnc = np.mean(time_103_dnc)#0.0644
mean_103_edc = np.mean(time_103_edc)#0.0578

time_104_bf = list()
time_104_dnc = list()
time_104_edc = list()

for i in range(0, 10):
   self_input = _inputgenerate(10000)
   start = time.time()
   _bruteforce('self_example.input')
   t = time.time() - start
   time_104_bf.append(t)
   start = time.time()
   _divideandconquer('self_example.input')
   t = time.time() - start
   time_104_dnc.append(t)
   start = time.time()
   _enhanceddnc('self_example.input')
   t = time.time() - start
   time_104_edc.append(t)
   
mean_104_bf = np.mean(time_104_bf)#158.23
mean_104_dnc = np.mean(time_104_dnc)#1.23
mean_104_edc = np.mean(time_104_edc)#1.11


time_105_bf = list()
time_105_dnc = list()
time_105_edc = list()

for i in range(0, 10):
   self_input = _inputgenerate(100000)
   #start = time.time()
   #_bruteforce('self_example.input')
   #t = time.time() - start
   #time_105_bf.append(t)
   start = time.time()
   _divideandconquer('self_example.input')
   t = time.time() - start
   time_105_dnc.append(t)
   start = time.time()
   _enhanceddnc('self_example.input')
   t = time.time() - start
   time_105_edc.append(t)
   
mean_105_bf = np.mean(time_105_bf)#?
mean_105_dnc = np.mean(time_105_dnc)#24.84
mean_105_edc = np.mean(time_105_edc)#19.46


















