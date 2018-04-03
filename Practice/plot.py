# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import numpy as np

def plot_color_curves(ax, lvl, X, Y, Z, line_type=None):
    if line_type is None:
        ax.plot(lvl, X, 'r')
        ax.plot(lvl, Y, 'g')
        ax.plot(lvl, Z, 'b')
    else:
        ax.plot(lvl, X, 'r'+line_type)
        ax.plot(lvl, Y, 'g'+line_type)
        ax.plot(lvl, Z, 'b'+line_type)

# loading data
file_path = 'data/blue_tone_EVT2-H34.txt'
blue = np.loadtxt(file_path, delimiter="\t", skiprows=1)
red = np.loadtxt(file_path.replace('blue', 'red'), delimiter="\t", skiprows=1)
green = np.loadtxt(file_path.replace('blue', 'green'), delimiter="\t", skiprows=1)

# separating columns
red_lvl = red[:, 0]
red_X = red[:, 3]
red_Y = red[:, 4]
red_Z = red[:, 5]
blue_lvl = blue[:, 2]
blue_X = blue[:, 3]
blue_Y = blue[:, 4]
blue_Z = blue[:, 5]
green_lvl = green[:, 1]
green_X = green[:, 3]
green_Y = green[:, 4]
green_Z = green[:, 5]

# # plotting raw data
# f = plt.figure()
# ax = f.add_subplot(131)
# plot_color_curves(ax, red_lvl, red_X, red_Y, red_Z)
# ax = f.add_subplot(132)
# plot_color_curves(ax, blue_lvl, blue_X, blue_Y, blue_Z)
# ax = f.add_subplot(133)
# plot_color_curves(ax, green_lvl, green_X, green_Y, green_Z)

# calculate normalized luminance
L_r = red_Y / np.max(red_Y)
L_g = green_Y / np.max(green_Y)
L_b = blue_Y / np.max(blue_Y)

# plotting normalized luminance
f = plt.figure()
ax = f.add_subplot(111)
plot_color_curves(ax, red_lvl, L_r, L_g, L_b)
plt.legend(['red lum', 'green lum', 'blue lum'])

### EVT1
file_path = 'data/blue_tone_EVT1-H34.txt'
blue2 = np.loadtxt(file_path, delimiter="\t", skiprows=1)
green2 = np.loadtxt(file_path.replace('blue', 'green'), delimiter="\t", skiprows=1)
red2 = np.loadtxt(file_path.replace('blue', 'red'), delimiter="\t", skiprows=1)


# separating columns
red_lvl = red2[:, 0]
red_X = red2[:, 3]
red_Y = red2[:, 4]
red_Z = red2[:, 5]
blue_lvl = blue2[:, 2]
blue_X = blue2[:, 3]
blue_Y = blue2[:, 4]
blue_Z = blue2[:, 5]
green_lvl = green2[:, 1]
green_X = green2[:, 3]
green_Y = green2[:, 4]
green_Z = green2[:, 5]

# calculate normalized luminance
L_r = red_Y / np.max(red_Y)
L_g = green_Y / np.max(green_Y)
L_b = blue_Y / np.max(blue_Y)

# plotting onto same figure as before, new axis
# ax2 = f.add_subplot(122)
plot_color_curves(ax, red_lvl, L_r, L_g, L_b, line_type='--')
plt.legend(['red lum', 'green lum', 'blue lum'])

plt.show()

# input("press enter to end")