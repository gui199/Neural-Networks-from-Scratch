#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 15:38:32 2020

@author: gui
https://www.youtube.com/watch?v=TEWy9vZcxW4&list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3&index=4
"""

#Neural Networks from Scratch - P.4 Batches, Layers, and Objects
import numpy as np

inputs =[ [1.0, 2.0, 3.0, 2.5],
        [2.0, 5.0, -1.0, 2.0] ,
        [-1.5, 2.7, 3.3, -0.8]
        ]

weights = [
        [0.2, 0.8, -0.5, 1.0 ],
        [0.5, -0.91, 0.26,-0.5 ],
        [-0.26, -0.27, 0.17, 0.87 ]
        ]

biases = [2.0, 3, 0.5 ]

layer_output = np.dot( inputs, np.array(weights).T )+biases

#print(layer_output)

weights2 = [
        [0.1, -0.14, 0.5 ],
        [-0.5, 0.12, -0.33 ],
        [-0.44, 0.73, -0.13 ]
        ]

biases2 = [-1, 2, -0.5 ]

layer_output2 = np.dot( layer_output, np.array(weights2).T )+biases2

print(layer_output2)