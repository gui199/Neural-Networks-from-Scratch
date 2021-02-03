#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 00:42:17 2020

@author: gui
https://www.youtube.com/watch?v=tMrbN67U9d4&list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3&index=3
"""

#Neural Networks from Scratch - P.3 The Dot Product

inputs = [1.0, 2.0, 3.0, 2.5]

weights = [
        [0.2, 0.8, -0.5, 1.0 ],
        [0.5, -0.91, 0.26,-0.5 ],
        [-0.26, -0.27, 0.17, 0.87 ]
        ]

biases = [2.0, 3, 0.5 ]

layer_output = [] # Output of current layer
for neuron_weights, neuron_bias in zip(weights, biases):
    neuron_output = 0 # Outputs of given neuron
    for n_input, weight in zip(inputs, neuron_weights):
        neuron_output +=  n_input * weight 
    neuron_output += neuron_bias
    layer_output.append(neuron_output)
    
print(layer_output)
        