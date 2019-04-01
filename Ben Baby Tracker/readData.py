# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

#Change these variables
filename_formula = "data/Benjamin Erlien_formula_removeparagraphs.csv"    
#filename_formula = "data/Benjamin Erlien_formula_ET.csv"    
title = 'Formula'

plt.figure()

# reading all lines into list of string. 
with open(filename_formula, 'r') as f:
    content = f.readlines()[1:] #returns a list of all of the lines

content = [x.strip() for x in content] #removes white space at beginning and end
content = [x.replace('"','') for x in content] #removes "
content = [x.replace('oz.','') for x in content] #removes oz.
content = [x.replace(' ','') for x in content] #removes spaces

#print(content)

name = []
date = []
time = []
amount = []
for line in content:
    splt = line.split(',')
    name.append(splt[0])
    date.append(datetime.strptime(splt[1], '%m/%d/%y').date()) 
    #strptime can handle nonleading zeros. strftime can't
    time.append(datetime.strptime(splt[2], '%H:%M%p').time())
    amount.append(float(splt[3]))

plt.scatter(date, amount, label="amount", color="y")
plt.xticks(rotation=70)

#print(date)
#print(time)
