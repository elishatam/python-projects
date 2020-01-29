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
import prepareData

#scrollbar: https://stackoverflow.com/questions/42622146/scrollbar-on-matplotlib-showing-page

class Page(tk.Frame):
    def __init__(self, parent, startDate, endDate):

        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.startDate = startDate
        self.endDate = endDate

        self.data = prepareData.Data(filename='1to6month.csv', 
                    startDate=self.startDate,
                    endDate=self.endDate)

        self.fig = plt.figure(1)
        self.fig.set_size_inches(w=8, h=5)
        self.ax = self.fig.add_subplot(111)    
        

        self.drawGraph(df = self.data.df)

        canvas = FigureCanvasTkAgg(self.fig, master=self)
        canvas.get_tk_widget().grid(row=1,column=0)

        toolbarFrame = tk.Frame(master=root)
        toolbarFrame.grid(row=2,column=0, sticky="W")
        #To use this toolbar with grid, need to put it in its own frame
        toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
        

        self.menuFrame = ttk.Labelframe(self, text=("Menu"))
        self.menuFrame.grid(row=0, column=0, sticky="NSW",
            padx=5, pady=2)
        self.addInMenuFrame()

    def onClose(self):
        print("closeGraph")
        self.destroy()
        self.parent.destroy()
        #plt.close('all')
        plt.close()
        
        self.csv_filename = str(dt.datetime.now().strftime("%Y%m%d_%H-%M"))+"_data.csv"
        #self.data.df.to_csv(self.csv_filename, index=False)

    def addInMenuFrame(self):
        labelStartDate = tk.Label(self.menuFrame, text="Start Date")
        labelStartDate.grid(row=0, column=0, sticky='W,E', padx=5, pady=2)

        self.startDateValue = tk.StringVar(value=self.startDate)
        startDateEntry = ttk.Entry(self.menuFrame, textvariable=self.startDateValue, 
            width=20)
        startDateEntry.grid(row=0, column=1, sticky="W,E", padx=5, pady=2)

        labelEndDate = tk.Label(self.menuFrame, text="End Date")
        labelEndDate.grid(row=1, column=0, sticky='W,E', padx=5, pady=2)
        self.endDateValue = tk.StringVar(value=self.endDate)
        endDateEntry = ttk.Entry(self.menuFrame, textvariable=self.endDateValue, 
            width=20)
        endDateEntry.grid(row=1, column=1, sticky="W,E", padx=5, pady=2)

        #Button to update graph
        self.btnUpdateGraph = tk.Button(self.menuFrame, text="Update Graph",
            command=lambda: self.updateGraph(startDate=self.startDateValue.get(),
                                            endDate=self.endDateValue.get())
            )
        self.btnUpdateGraph.grid(row=1, column=2, sticky="W")

        #First 2 weeks Button
        self.btn2Weeks = tk.Button(self.menuFrame, text="2 weeks", 
            command=lambda: self.updateGraph(startDate="2017-08-02",
                                             endDate="2017-08-16"))
        self.btn2Weeks.grid(row=0, column=3, sticky="WE")

        #Month 1 Button
        self.btnMonth1 = tk.Button(self.menuFrame, text="Month 1", 
            command=lambda: self.updateGraph(startDate="2017-08-02",
                                             endDate="2017-09-02"))
        self.btnMonth1.grid(row=0, column=4, sticky="WE")

        #Month 2 Button
        self.btnMonth2 = tk.Button(self.menuFrame, text="Month 2", 
            command=lambda: self.updateGraph(startDate="2017-09-02",
                                             endDate="2017-10-02"))
        self.btnMonth2.grid(row=0, column=5, sticky="WE")

        #Month 3 Button
        self.btnMonth3 = tk.Button(self.menuFrame, text="Month 3", 
            command=lambda: self.updateGraph(startDate="2017-10-02",
                                             endDate="2017-11-02"))
        self.btnMonth3.grid(row=1, column=3, sticky="WE")

    def updateGraph(self, startDate, endDate):
        print("in UpdateGraph")
        
        self.data = prepareData.Data(filename='1to6month.csv', 
                    startDate=startDate,
                    endDate=endDate)
        
        df = self.data.df
        #plt.cla() #clear axis
        #self.setupAxis()
        self.drawGraph(df = df)
        
        #Update values in entry
        self.startDateValue.set(startDate)
        self.endDateValue.set(endDate)


    def drawGraph(self, df):
        plt.cla() #clear axis

        self.ax.xaxis.set_major_formatter(dtm.DateFormatter('%I:%M %p'))
        self.ax.xaxis.set_major_locator(dtm.HourLocator(byhour=range(0,24,4)))
        self.ax.xaxis.set_minor_locator(dtm.HourLocator(byhour=range(0,24,1)))
        self.ax.xaxis.tick_top()
        self.ax.xaxis.set_label_position('top')

        self.colors = {
            'Sleep': '#cdc8b1',
            'Nursing': '#ff8c00',
            'Wet': '#00bfff',
            'Dirty': '#00bfff',
            'Mixed': '#00bfff',
            'Dry': '#00bfff',
            'BottleFormula': '#ffffff',
            'BottlePumped': '#ff8c00',
            'Eat': '#F3050D',
            'Work': '#7fff00'
        }

        #ax = plt.hlines(df.DateString, dtm.date2num(df.Time_SameDate2), dtm.date2num(df.EndTime_SameDate2), linewidth=15, color=df['Resource'].map(self.colors))
        
        #self.ax = plt.hlines(df.DateString, dtm.date2num(df.Time_SameDate2), dtm.date2num(df.EndTime_SameDate2), linewidth=8, color=df['Resource'].map(self.colors))
        #Had to change 'self.ax' to another name. It was redefining self.ax to be a list returned by the hlines command
        #https://stackoverflow.com/questions/48376000/matplotlib-plotting-attributeerror-list-object-has-no-attribute-xaxis
        lines = plt.hlines(y=df.DateString, 
                           xmin=dtm.date2num(df.Time_SameDate2), 
                           xmax=dtm.date2num(df.EndTime_SameDate2), 
                           linewidth=8, 
                           color=df['Resource'].map(self.colors))

        
        #Make own legend: https://stackoverflow.com/questions/39500265/manually-add-legend-items-python-matplotlib
        #red_patch=mpatches.Patch(color='red', label='Sleep')
        sleep_patch=mpatches.Patch(color=self.colors["Sleep"], label='Sleep')
        nursing_patch=mpatches.Patch(color=self.colors["Nursing"], label='Nursing')
        diaper_patch=mpatches.Patch(color=self.colors["Wet"], label='Diaper')
        bottle_patch=mpatches.Patch(color=self.colors["BottleFormula"], label='Bottle')
        eat_patch=mpatches.Patch(color=self.colors["Eat"], label='Eat')
        work_patch=mpatches.Patch(color=self.colors["Work"], label='Personal')

        
        plt.legend(handles=[sleep_patch,nursing_patch, diaper_patch, eat_patch, work_patch], bbox_to_anchor=(0., -.1, 1, .102), loc=3,
        #plt.legend(handles=[sleep_patch, nursing_patch, diaper_patch, eat_patch, work_patch], bbox_to_anchor=(0., 1.02, 1, .102), loc=3,
                   ncol=5, mode="expand", borderaxespad=0.) #bbox_to_anchor=(0.9, 0.3)
        #plt.legend(handles=[sleep_patch, nursing_patch, diaper_patch, bottle_patch], bbox_to_anchor=(1.05, 1))
        #plt.margins(.15)  #So xticks start at 12:00am
        plt.xticks(rotation=90)
        self.fig.tight_layout()  #Border will fit around axis
        plt.gca().invert_yaxis()
        plt.subplots_adjust(bottom=0.13)
        #plt.subplots_adjust(bottom=0.19, top=0.92)
        #plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
        #plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True
        #plt.show()
        #plt.ion()
        #plt.draw()
        
        #self.ax.plot()

        #https://stackoverflow.com/questions/4098131/how-to-update-a-plot-in-matplotlib
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

    def resize(self, event):
        
        print(root.winfo_width(), root.winfo_height())
        self.fig.set_size_inches(w=root.winfo_width()/120, h=root.winfo_height()/120)
        self.drawGraph(df=self.data.df)
  


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Graph")
    app = Page(parent=root, startDate="2017-9-10", endDate="2017-9-25")  #This is to test the pageEngineer
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
