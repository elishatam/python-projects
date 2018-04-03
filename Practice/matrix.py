#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 10:32:52 2018

@author: elishatam
https://engineering.purdue.edu/~bouman/ece637/notes/pdf/ColorSpaces.pdf
"""

import numpy as np
from scipy.linalg import solve

# A = np.random.random((3,3))
# b = np.random.random(3)
M = np.array([[0.67,0.21,0.14],[0.33,0.71,0.08],[0.0,0.08,0.78]])
b = np.array([1,1,1])

x = solve(M, b)
print x
# x = [0.98672566 0.8147914  1.19848293]
# Confirm should equal [1 1 1]
print M.dot(x)

C = [[0.9867,0.0,0.0],[0.0,0.8148,0.0],[0.0,0.0,1.1985]]

print M.dot(C)
#[[0.66110619 0.17110619 0.16778761]
# [0.32561947 0.5785019  0.09587863]
# [0.         0.06518331 0.93481669]]


