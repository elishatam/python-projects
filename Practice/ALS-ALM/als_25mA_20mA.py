#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 17:10:03 2018

@author: elishatam
"""

import matplotlib.pyplot as plt
import numpy as np

def graph(formula, x_range):
    x = np.array(x_range)
    y = eval(formula)
    plt.plot(x,y)
    plt.show()

setting= [25,65,85,95,110,125,150,155,205,255]
lum_25mA = [62.93,160.9,207.8,230.9,264.6,298.1,352.8,363.2,469.1,571.7]
lum_20mA = [50.47,130.1,168.6,187.5,215.5,243.1,288.7,297.5,385.9,474.1]

setting2 =[32,85,111,123,141,160,189,195,253,308]


#lux = [0,6,17,34,57,85,120,145,228,250,370]
#twoD_25mA = [25,65,85,95,110,125,150,155,205,211,255]
#twoD_20mA = [32,85,111,123,141,160,189,195,253,255,308]

plt.gcf().clear()
plt.plot(setting,lum_25mA,'b.',markersize=12, label="twoD_25mA")
plt.plot(setting,lum_20mA,'g.',markersize=12, label="twoD_20mA")
plt.plot(setting2,lum_25mA,'r.',markersize=12, label="twoD_20mA")

graph('2.212*x+7.63', range(0,300))
graph('1.84*x+4.47', range(0,300))

plt.show()