#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 01:07:49 2020

@author: gui
"""

a = [1, 2, 3]
b = [2, 3, 4]

dot_product = a[0]*b[0]+ a[1]*b[1]+ a[2]*b[2]
print(dot_product)

import numpy as np
dot_product = np.dot(a, b)
print(dot_product)

vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])

dot_product = np.dot(vector_a, vector_b)
print(dot_product)