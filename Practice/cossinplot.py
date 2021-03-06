#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 14:29:51 2018

@author: elishatam
https://www.labri.fr/perso/nrougier/teaching/matplotlib/
"""

import numpy as np
import matplotlib.pyplot as plt

# Create a new figure of size 8x6 points, using 100 dots per inch
fig1 = plt.figure(figsize=(10,6), dpi=80)

#Create a new subplot from a grid of 1x1
plt.subplot(111)

#ax1 = fig1.add_subplot(111)
#ax1.plot(x,y)

#z = np.sin(x)
#fig2 = plt.figure()
#ax2 = fig2.add_subplot(111)
#ax2.plot(x,z)

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)

# Plot cosine using blue color with a continuous line of width 1 (pixels)
plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cosine")

# Plot sine using green color with a continuous line of width 1 (pixels)
plt.plot(X, S, color="green", linewidth=2.5, linestyle="--", label="sine")

# Plot legend
plt.legend(loc='upper left', frameon=True)

# Set x limits
plt.xlim(X.min()*1.1,X.max()*1.1)

# Set x ticks
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

#Set y limits
plt.ylim(C.min()*1.1, C.max()*1.1)

# Set y ticks
plt.yticks([-1,0,+1], [r'$-1$', r'$0$', r'$+1$'])

# Place spines in the middle of the graph, not default around the border
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

# Annotate some interesting points (2pi/3)
t = 2*np.pi/3
plt.plot([t,t],[0,np.cos(t)], color='blue', linewidth=1.5, linestyle="--")
plt.scatter([t,],[np.cos(t),], 50, color='blue')
plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, np.sin(t)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.plot([t,t],[0,np.sin(t)], color ='red', linewidth=1.5, linestyle="--")
plt.scatter([t,],[np.sin(t),], 50, color ='red')
plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

# Make tick labels bigger with a semi-transparent white background
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='red', edgecolor='None', alpha=0.15 ))

# Save figure using 72 dots per inch
#savefig("../figures/sinplot2.png", dpi=72)


plt.show()

