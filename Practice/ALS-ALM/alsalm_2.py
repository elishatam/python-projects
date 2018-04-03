#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 13:45:34 2018

@author: elishatam
"""

import matplotlib.pyplot as plt
import numpy as np


def graph(formula, x_range):
    x = np.array(x_range)
    y = eval(formula)
    plt.plot(x,y)
    plt.show()
    

    
# "r" forces python to interpret the info literally
# Note that loadtxt *assumes* your data is in numeric form, 
# so if there's a header with column names, you should remove that before reading
data=np.loadtxt(r"/Users/elishatam/Documents/elisha/Python Course/Practice/ALS-ALM/alsalm_2.csv")
drmeter=data[:,0]
evt2h41=data[:,1]
evt2h43=data[:,2]

data2=np.loadtxt(r"/Users/elishatam/Documents/elisha/Python Course/Practice/ALS-ALM/EVT2H38_EVT2H20.csv")
drmeter2=data2[:,0]
evt2h38=data2[:,1]
evt2h20=data2[:,2]

als_alm_409_conv = 20.0     # Modify this to try a different slope. Conversion between ALS to ALM
#slope = 0.04       # 
slope = 1/als_alm_409_conv
eqn = str(slope) + '*x'
inv_eqn = str(als_alm_409_conv) + '*y'

als_alm_conv_old = 70.0     # Modify this to try a different slope. Conversion between ALS to ALM
slope_old = 1/als_alm_conv_old
eqn_old = str(slope_old) + '*x'
inv_eqn_old = str(als_alm_conv_old) + '*y'

plt.gcf().clear()
plt.plot(drmeter,evt2h41,'b.',markersize=12, label="EVT2H41 ALS, build 409")
plt.plot(drmeter,evt2h43,'g.',markersize=12, label="EVT2H43 ALS, build 409")
plt.plot(drmeter2,evt2h38,'r.',markersize=12, label="EVT2H38 ALS")
plt.plot(drmeter2,evt2h20,'y.',markersize=12, label="EVT2H20 ALS")
graph(eqn, range(0,6000))

#graph(eqn_old, range(0,6000))

#graph('0.015*x', range(0,6000))
 
plt.title('ALS v. ALM')
plt.xlabel('Dr. Meter')
plt.ylabel('ALS')
plt.xlim(0,1000)
plt.ylim(0,500)
plt.annotate('y = ' + eqn , xy=(3000,1), xytext=(4000,300), color = 'b')
plt.annotate('x = ' + inv_eqn , xy=(3000,1), xytext=(4000,275), color = 'b')
plt.axvline(x=540, color = 'c')
plt.annotate('Inside', xy=(0,0), xytext=(10,300), color ='c')
plt.annotate('Leia', xy=(0,0), xytext=(10,280), color ='c')
plt.annotate('Outside', xy=(0,0), xytext=(1000,300), color ='c')
plt.annotate('Leia', xy=(0,0), xytext=(1000,280), color ='c')
# Plot legend
plt.legend(loc='upper right', frameon=True)
plt.annotate('y = ' + eqn , xy=(3000,1), xytext=(4000,300), color = 'b')
plt.annotate('x = ' + inv_eqn , xy=(3000,1), xytext=(4000,275), color = 'b')

