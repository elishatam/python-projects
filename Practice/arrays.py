#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 20:46:55 2018

@author: elishatam
"""

import numpy as np

# 1) Using "arange", create an array called "myarray" that has
# the same length as the number of letters in your last name and 
# counts up from 1
myarray=np.arange(1.,4)
print myarray

# 2) Create a 2nd array that is the square root of the first.
#rootarray=np.array([np.sqrt(myarray[0]),np.sqrt(myarray[1]),np.sqrt(myarray[2])])

rootarray = myarray
for i in range (0,len(myarray)):
    rootarray[i]=np.sqrt(myarray[i])
print rootarray

