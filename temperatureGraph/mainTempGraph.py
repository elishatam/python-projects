#open csv file
#graph
#Highest temp in red. Annotate
#Coolest temp in blue. Annotate
#before O, bBT = 97 to 97.5F
#During O, prog is released. Raises tmp 0.5d 1-2days later
#Stays high until next cycle. If p, will stay high
#most fertile 2-3days before temp rises
#Identify first day
#Count each day
#Annotate temperature and comments

import matplotlib
from matplotlib import pyplot as plt
import matplotlib.dates as dtm
import matplotlib.patches as mpatches
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np
import tkinter as tk
from tkinter import ttk
import datetime as dt
import pandas as pd
import time
from datetime import datetime, date, timedelta

#scrollbar: https://stackoverflow.com/questions/42622146/scrollbar-on-matplotlib-showing-page

class Page(tk.Frame):
    def __init__(self, parent, filename):

        tk.Frame.__init__(self, parent)
        self.parent = parent
        drawGraphFlag = 1

        
        if drawGraphFlag == 1:
            #Prepare Tk GUI for graph
            self.fig = plt.figure(1)
            self.ax = self.fig.add_subplot(111)
            self.canvas = FigureCanvasTkAgg(self.fig, master=self)
            self.canvas.get_tk_widget().grid(row=0,column=0)

            #Add in toolbar
            toolbarFrame = tk.Frame(master=root)
            toolbarFrame.grid(row=2,column=0, sticky="W")
            #To use this toolbar with grid, need to put it in its own frame
            toolbar = NavigationToolbar2Tk(self.canvas, toolbarFrame)

        #Open file
        self.filename = 'data/2020_02.csv'
        self.df = pd.read_csv(self.filename)

        self.prepareData()

        if drawGraphFlag == 1:
            self.drawGraph()

        #BBT spike day
        #print("BBT Spike Day: "+str(self.BBTSpikeDay))
        #Ov day
        #print("The current Ov Day (1-2day before BBT):"+str(self.BBTSpikeDay-2))
        #Luteal Phase length
        #Next Ovulation day if 1st day of period is

    def prepareData(self):
        self.df.Date = pd.to_datetime(self.df.Date)
        self.df['DateOnly'] = self.df['Date'].dt.date
        firstDateValue = self.df.iloc[0]['DateOnly'] #get first entry in Date
        self.df['DayCount'] = (self.df.DateOnly - firstDateValue).dt.days

        #Look for Coverline if dataframe length > 9
        #print("length of df Temp: " + str(len(self.df['Temp (F)'])))
        if len(self.df['Temp (F)']) > 9:
            if self.foundCoverlineTempValue():
                self.drawCoverlineFlag = 1
            else:
                self.drawCoverlineFlag = 0
            self.setColorByTemp(tempValue=self.coverlineValue)
        else:
            self.drawCoverlineFlag = 0
            self.setColorByTemp(tempValue=98)

            

        self.df.info()
        print(self.df)

    def drawGraph(self):
        x = self.df['DayCount']
        y = self.df['Temp (F)']
        self.ax.scatter(x,y, c=self.df['Color'])
        self.ax.set_xlabel('Elapsed Time (s)')
        self.ax.set_ylabel('Temp (F)')

        #Plot horizontal line at coverline
        if self.drawCoverlineFlag == 1:
            self.ax.axhline(y=self.coverlineValue+0.1, color="green", linestyle='--')

    def setColorByTemp(self, tempValue):
        self.df['Color'] = "blue"
        #For temperatures > X, make color red
        #https://stackoverflow.com/questions/17241004/how-do-i-convert-a-pandas-series-or-index-to-a-numpy-array
        #https://stackoverflow.com/questions/17241004/how-do-i-get-a-dataframe-index-series-column-as-an-array-or-list
        #Add 0.1 offset because I don't want the low6min to be highlighted
        higherTemp_indices = (self.df[(self.df["Temp (F)"] > tempValue+0.1)].index.values) 
        for indexA in higherTemp_indices:
            self.df.loc[indexA, 'Color'] = "red"

        #print(higherTemp_indices) 
        print(self.df)

    def foundCoverlineTempValue(self):
        #the first 6 low consecutive temps must be lower than the next 3
        #higher consecutive temps.
        #The gap between the highest of the previous 6 temps and the lowest
        #of the next 3 temps is >= 0.5F
        for i,j in enumerate(range(1,16)):
            #Find i and j adjacent elements that have a 0.5F difference
            if (self.df['Temp (F)'][j] - self.df['Temp (F)'][i] > 0.5):
                #group previous 6 values
                self.low6List = [self.df['Temp (F)'][i-5], 
                                   self.df['Temp (F)'][i-4],
                                   self.df['Temp (F)'][i-3],
                                   self.df['Temp (F)'][i-2],
                                   self.df['Temp (F)'][i-1],
                                   self.df['Temp (F)'][i],
                                  ]
                #find highest of 6 values
                self.low6List_max = max(self.low6List)
                
                #group next 3 values
                self.high3List = [self.df['Temp (F)'][i+1], 
                                   self.df['Temp (F)'][i+2],
                                   self.df['Temp (F)'][i+3],
                                   ]
                #find lowest of 3 values
                self.high3List_min = min(self.high3List)

                self.df.loc[j, 'BBT Spike'] = "BBT Spike" #j=i+1
                self.BBTSpikeDay = self.df['DayCount'][j]
                self.coverlineValue = self.df['Temp (F)'][i]
                
        #Test for coverline
        #The first 6 low consecutive temps must be lower than the next 3 high temps
        for value in self.low6List:
            if value < self.high3List_min:
                coverlineFlag = True
            else:
                self.coverlineFlag = False

        if (self.high3List_min - self.low6List_max >= 0.5):
            coverlineFlag = True
            print("coverlineValue: " + str(self.coverlineValue))
            #print("low6List: " + str(self.low6List) + ". Max: " + str(self.low6List_max))

        else: 
            coverlineFlag = False

        if coverlineFlag == True:
            return True
        else:
            return False


        

    def onClose(self):
        print("closeGraph")
        self.destroy()
        self.parent.destroy()
        #plt.close('all')
        plt.close()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Graph")
    app = Page(parent=root, filename="2020_02.csv")  #This is to test the pageEngineer
    app.grid(row=0, column=0, sticky="W")
    root.protocol("WM_DELETE_WINDOW",app.onClose)

    while True:
        root.update_idletasks()
        root.update()  #This blocks
