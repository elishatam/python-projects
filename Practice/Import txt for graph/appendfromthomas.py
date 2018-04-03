#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 16:56:04 2018

@author: elishatam
"""

f = open('test.txt', 'w')
f.write('<header xml stuff>')
a = [0, 0, 1023, 1023]
a_str = [str(a_element) +',' for a_element in a]
s = "".join(a_str) # with last comma
s_nocomma = "".join(a_str)[:-1] # without last comma
f.write(s)
f.close()