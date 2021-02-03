#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 01:21:36 2020

@author: gui
"""

inputs = [1.0, 2.0, 3.0, 2.5]

weights = [
        [0.2, 0.8, -0.5, 1.0 ],
        [0.5, -0.91, 0.26,-0.5 ],
        [-0.26, -0.27, 0.17, 0.87 ]
        ]

biases = [2.0, 3, 0.5 ]

import numpy as np

#np.dot(inputs, weights[0])+biases[0]
#np.dot(inputs, weights[1])+biases[1]
#np.dot(inputs, weights[2])+biases[2]

layer_output = np.dot(weights, inputs )+biases

print(layer_output)

