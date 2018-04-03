#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 14:29:43 2018

@author: elishatam
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(5)
y = np.exp(x)
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.plot(x,y)

z = np.sin(x)
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.plot(x,z)

w = np.cos(x)
ax1.plot(x,w)