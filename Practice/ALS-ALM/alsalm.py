#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 13:27:15 2018

@author: elishatam
"""

import matplotlib.pyplot as plt
import numpy as np
#import math
from scipy.optimize import curve_fit

plt.gcf().clear()
data1 = np.genfromtxt('ALSALM.csv', delimiter=',', skip_header=1,
                     names=['x1', 'y1', 'z1'])
#plt.scatter(data1['x1'], data1['y1'], color='r', label='1')
#plt.scatter(data1['x1'], data1['z1'], color='b', label='2')

plt.xlabel('Dr. Meter')
plt.ylabel('ALS')
plt.title('Dr. Meter v. ALS')
#plt.legend()
#plt.show()

#plateau - logistic function. Sigmoid (upper and lower bounds = population growth curves)
#logistics function - define function to create this
#scipy.optimize.curve_fit

#https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html
#L = curve's max value = 80
#x0 = x-value of the sigmoid's midpoint = 0
#k = steepness of the curve = 2?
"""
def func(x, L, x0, k):
    return L*np.exp(-x0*x) + k

xdata=np.linspace(0,4,50)
y = func(xdata, 2.5, 1.3, 0.5)
np.random.seed(1729)
y_noise=0.2*np.random.normal(size=xdata.size)
ydata = y+y_noise
plt.plot(xdata, ydata, 'b-', label='data')
popt, pcov = curve_fit(func, xdata, ydata)
plt.plot(xdata,func(xdata, *popt),'r-', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
"""

def func(x, L, x0, k):
    #exp = np.exp(-k*(x-x0))
    #exp = x+L+x0
    #denom = 1 + exp
    #return L/denom
    #return L*np.exp(-x0*x) + k
    return (L / (1+np.exp(-k*(x-x0)))) - 60
    
xdata = np.linspace(0, 100, 100)
ydata = func(xdata, 120, 0, 0.12)
popt, pcov = curve_fit(func, xdata, ydata)
print popt
#plt.plot(xdata, func(xdata, *popt), 'r-', label='fit: L=80, x0 = 0, k=2' % tuple(popt))
plt.plot(xdata, func(xdata, *popt), 'r-')
#plt.show()


"""
# calculate polynomial
z = np.polyfit(data1['x1'], data1['y1'], 2)
f = np.poly1d(z)

x_min = np.min(data1['x1'])
x_max = np.max(data1['x1'])

# calculate new x's and y's
#x_new = np.linspace(x[0], x[-1], 50) #take first thru last element
x_new = np.linspace(x_min, x_max, 50)
y_new = f(x_new)

#plt.plot(x,y,'o', x_new, y_new)
#plt.xlim([x[0]-1, x[-1] + 1 ])

plt.plot(x_new, y_new)
#plt.scatter(np.log(data1['x1']), np.log(data1['y1']), color='r', label='1')
#plt.scatter(np.log(data1['x1']), np.log(data1['z1']), color='b', label='2')
"""