#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 12:39:01 2020

@author: gui
https://www.youtube.com/watch?v=lGLto9Xd7bU&list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3
"""

#Neural Networks from Scratch - P.1 Intro and Neuron Code

inputs = [1.2, 5.1, 2.1]
weights = [3.1, 2.1, 8.7]
bias = 3        

output = inputs[0]*weights[0]+ inputs[1]*weights[1]+ inputs[2]*weights[2]+bias

print(output)