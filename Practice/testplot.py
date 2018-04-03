#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 17:29:25 2018

@author: elishatam
https://users.physics.unc.edu/~sheila/pythontutorial.html
http://cs231n.github.io/python-numpy-tutorial/#matplotlib-plotting
"""

import matplotlib.pyplot as plt
import numpy as np
# "r" forces python to interpret the info literally
# Note that loadtxt *assumes* your data is in numeric form, 
# so if there's a header with column names, you should remove that before reading
data=np.loadtxt(r"/Users/elishatam/Documents/elisha/Python Course/Practice/testdata.in")
temperature=data[:,0]
humidity=data[:,1]
plt.plot(humidity,temperature,'b.',markersize=12)
plt.title('Elisha Tam Python Tutorial')
plt.xlabel('humidity (%)')
plt.ylabel('temperature (F)')
plt.xlim(10,60)
plt.ylim(80,100)
# Select points where humidity < 20%
sel=np.where(humidity<20)
print sel
print humidity[sel]
print temperature[sel]

#plot data where temp (80,100) and humidity (10-40)
sel2=np.where((temperature > 80) & (temperature < 100))
plt.plot(humidity[sel2],temperature[sel2],'g*',markersize=15)  
sel3=np.where((humidity > 10) & (humidity < 40))
plt.plot(humidity[sel3],temperature[sel3],'r+',markersize=15)  

  