#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 13:45:34 2018
Use this graph to determine the conversion between ALM and ALS
@author: elishatam
"""

import matplotlib.pyplot as plt
import numpy as np


def graph(formula, x_range):
    x = np.array(x_range)
    y = eval(formula)
    plt.plot(x,y)
    plt.show()
    
def set_graph_layout(xmax,ymax):
    plt.xlim(0,xmax) #xmax=6000
    #plt.xlim(0,1000)
    plt.ylim(0,ymax) #ymax=400
    plt.annotate('Inside', xy=(0,0), xytext=(10,300), color ='c')
    plt.annotate('Leia', xy=(0,0), xytext=(10,280), color ='c')
    plt.annotate('Outside', xy=(0,0), xytext=(1000,300), color ='c')
    plt.annotate('Leia', xy=(0,0), xytext=(1000,280), color ='c')
    plt.axvline(x=540, color = 'c')
    plt.legend(loc='upper right', frameon=True)
    plt.xlabel('Dr. Meter')
    plt.ylabel('ALS')
    #David's ALS v. ALM plot
    plt.plot([-1, 113, 341, 683, 1138, 1708, 2391, 2904, 4555, 7403], [0, 5, 14, 27, 46, 68, 96, 116, 182, 296], 'm--')
    plt.annotate('x=25*y (David)', xy=(3000,1), xytext=(4000,130), color = 'm')

def slopeformula(conv):
    slope = 1/conv
    

# "r" forces python to interpret the info literally
# Note that loadtxt *assumes* your data is in numeric form, 
# so if there's a header with column names, you should remove that before reading
#data=np.loadtxt(r"/Users/elishatam/Documents/elisha/Python Course/Practice/ALS-ALM/alsalm_2.csv")
data=np.loadtxt(r"alsalm_2.csv")
drmeter=data[:,0]
evt2h41=data[:,1]
evt2h43=data[:,2]

#data2=np.loadtxt(r"/Users/elishatam/Documents/elisha/Python Course/Practice/ALS-ALM/EVT2H38_EVT2H20.csv")
data2=np.loadtxt(r"EVT2H38_EVT2H20.csv")
drmeter2=data2[:,0]
evt2h38=data2[:,1]
evt2h20=data2[:,2]

#With Develop Build 232. ALS readings are much higher
data3=np.loadtxt(r"H43_H46_H21.csv", delimiter=',',skiprows=1)
drmeter3=data3[:,0]
evt2h43_2=data3[:,1]
evt2h21=data3[:,2]
evt2h46=data3[:,3]

# First Plot's Equation
als_alm_409_conv = 20.0     # Modify this to try a different slope. Conversion between ALS to ALM
#slope = 0.04       # 
slope = 1/als_alm_409_conv
eqn = str(slope) + '*x'
inv_eqn = str(als_alm_409_conv) + '*y'

## 2nd Plot's Equation
#als_alm_conv_old = 70.0     # Modify this to try a different slope. Conversion between ALS to ALM
#slope_old = 1/als_alm_conv_old
#eqn_old = str(slope_old) + '*x'
#inv_eqn_old = str(als_alm_conv_old) + '*y'

# 3rd Plot's Equation
als_alm_d232_conv = 5.0     # Modify this to try a different slope. Conversion between ALS to ALM
slope3 = 1/als_alm_d232_conv
eqn3 = str(slope3) + '*x'
inv_eqn3 = str(als_alm_d232_conv) + '*y'

# First Plot
plt.gcf().clear()
plt.figure(1)

plt.subplot(311)
plt.plot(drmeter,evt2h41,'b.',markersize=12, label="EVT2H41 ALS, build 409")
plt.plot(drmeter,evt2h43,'g.',markersize=12, label="EVT2H43 ALS, build 409")
plt.title('ALS v. ALM')
graph(eqn, range(0,6000))

plt.annotate('y = ' + eqn , xy=(3000,1), xytext=(4000,300), color = 'b')
plt.annotate('x = ' + inv_eqn , xy=(3000,1), xytext=(4000,275), color = 'b')
plt.annotate('y = ' + eqn , xy=(3000,1), xytext=(4000,300), color = 'b')
plt.annotate('x = ' + inv_eqn , xy=(3000,1), xytext=(4000,275), color = 'b')
set_graph_layout(6000,400)


## Second Plot
#plt.subplot(312)
#plt.plot(drmeter2,evt2h38,'r.',markersize=12, label="EVT2H38 ALS")
#plt.plot(drmeter2,evt2h20,'y.',markersize=12, label="EVT2H20 ALS")
#graph(eqn_old, range(0,6000))
#set_graph_layout(6000,400)

# Third Plot
plt.subplot(313)
plt.plot(drmeter3,evt2h43_2,'r.',markersize=12, label="EVT2H43")
#plt.plot(drmeter3,evt2h21,'y.',markersize=12, label="EVT2H21")
plt.plot(drmeter3,evt2h46,'b.',markersize=12, label="EVT2H21")
graph(eqn3, range(0,10000))
set_graph_layout(10000,3000)



