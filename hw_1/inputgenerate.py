#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 09:45:48 2017

@author: wangchunxiao
"""
import random as rn
import numpy as np

def _inputgenerate(n):
    ar = np.arange(0, n, 0.1)
    x_cor = rn.sample(list(ar), n)
    y_cor = rn.sample(list(ar), n)
    with open ('self_example.input', 'w') as f:
        for i in range(0, n):
            print(x_cor[i], y_cor[i], file = f)
    f.close()
            
    