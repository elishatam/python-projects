#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 11:59:47 2018

@author: elishatam
"""

import matplotlib.pyplot as plt
import numpy as np

# "r" forces python to interpret the info literally
# Note that loadtxt *assumes* your data is in numeric form, 
# so if there's a header with column names, you should remove that before reading
data=np.loadtxt(r"/Users/elishatam/Documents/Repos/python-projects/Practice/AverageBacklightColors/EVT2PhonesforRed.csv", delimiter=',',skiprows=1)
native_x=data[:,0]
native_y=data[:,1]
native_lum=data[:,2]
norm_r=data[:,3]
norm_g=data[:,4]
norm_b=data[:,5]
lum_loss=data[:,6]
norm_r_gamma=data[:,7]
norm_g_gamma=data[:,8]
norm_b_gamma=data[:,9]

plt.gcf().clear()
plt.figure(1)
plt.subplot(211)
plt.plot(native_x,native_y,'b.',markersize=12, label="Native_White")
plt.plot(np.mean(native_x),np.mean(native_y),'r.',markersize=12)
#plt.xlim(0,1)
#plt.ylim(0,1)

plt.subplot(212)
plt.plot(norm_r,norm_g,'r.',markersize=12, label="Native_White")

