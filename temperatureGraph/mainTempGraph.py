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

        #Prepare Tk gui for graph
        self.fig = plt.figure(1)
        self.ax = self.fig.add_subplot(111)
        canvas = FigureCanvasTkAgg(self.fig, master=self)
        canvas.get_tk_widget().grid(row=0,column=0)

        #Add in toolbar
        toolbarFrame = tk.Frame(master=root)
        toolbarFrame.grid(row=2,column=0, sticky="W")
        #To use this toolbar with grid, need to put it in its own frame
        toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)

        #Open file
        self.filename = 'data/2020_02.csv'
       	self.df = pd.read_csv(self.filename)

        self.prepareData()
        self.drawGraph()

    def prepareData(self):
    	self.df.Date = pd.to_datetime(self.df.Date)

    def drawGraph(self):

    	x = self.df['Date']
    	y = self.df['Temp (F)']
    	#plt.plot(x,y)
    	#plt.show()
    	self.ax.plot(x,y)
    	self.fig.canvas.draw()
    	self.fig.canvas.flush_events()

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
    #w=1000
    #h=650
    #x=1040
    #y=700
    #root.geometry('%dx%d+%d+%d' % (w,h,x,y)) #Position window
    root.protocol("WM_DELETE_WINDOW",app.onClose)
    #root.bind("<Configure>", app.resize)

    while True:
        root.update_idletasks()
        root.update()  #This blocks
