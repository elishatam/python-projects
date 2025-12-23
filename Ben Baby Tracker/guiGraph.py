import matplotlib

import matplotlib.dates as dtm
import matplotlib.patches as mpatches
matplotlib.use("TkAgg")
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk
import datetime as dt
import prepareData
import widgetMenu
import widgetDays

#scrollbar: https://stackoverflow.com/questions/42622146/scrollbar-on-matplotlib-showing-page

class Page(tk.Frame):
    def __init__(self, parent, startDate, endDate):

        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.startDate = startDate
        self.endDate = endDate
        self.obj_days_forGraph = []  #initialize empty list

        self.data = prepareData.Data(filename='1to6month.csv', 
                    startDate=self.startDate,
                    endDate=self.endDate,
                    obj_days_forGraph = self.obj_days_forGraph)

        self.obj_days_forGraph = self.data.getObjDaysForGraph()  #Need to do this. Is there a way around this?
        #print(self.obj_days_forGraph)    #This prints after getObjDaysForGraph(). Otherwise empty

        self.fig = plt.figure(1)
        self.fig.set_size_inches(w=8, h=5)
        self.ax = self.fig.add_subplot(111)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)

        self.menuWidget = widgetMenu.menuWidget(parent=self, 
                        initStartDate=self.startDate, initEndDate=self.endDate,
                        originalDataFirstDate=self.data.originalFirstDate,
                        originalDataLastDate=self.data.originalLastDate)
        self.menuWidget.grid(row=0, column=0, sticky="NESW", padx=5, pady=2)

        self.drawGraph(df = self.data.df)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().grid(row=1, column=0, sticky="NESW")
        self.canvas.get_tk_widget().bind("<Configure>", self.resize, add="+")

        toolbarFrame = tk.Frame(master=self)
        toolbarFrame.grid(row=2, column=0, sticky="W")
        #To use this toolbar with grid, need to put it in its own frame
        #toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
        
        self.daysWidget = widgetDays.daysWidget(parent=self, obj_days_forGraph=self.obj_days_forGraph)

        self.daysWidget.grid(row=1, column=1, sticky="NESW", padx=5, pady=2)


    def onClose(self):
        print("closeGraph")
        self.destroy()
        self.parent.destroy()
        #plt.close('all')
        plt.close()
        
        #self.csv_filename = str(dt.datetime.now().strftime("%Y%m%d_%H-%M"))+"_data.csv"
        #self.data.df.to_csv(self.csv_filename, index=False)


    def updateGraph(self, startDate, endDate):
        print("in UpdateGraph")

        self.data = prepareData.Data(filename='1to6month.csv', 
                    startDate=startDate,
                    endDate=endDate,
                    obj_days_forGraph = self.obj_days_forGraph)
        
        df = self.data.df

        self.obj_days_forGraph = self.data.getObjDaysForGraph()  #Need to do this. Is there a way around this?

        self.daysWidget.updateChart(obj_days_forGraph=self.obj_days_forGraph)
        #plt.cla() #clear axis
        #self.setupAxis()
        self.drawGraph(df = df)



    def drawGraph(self, df):
        self.ax.clear() #clear axis

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
        lines = self.ax.hlines(y=df.DateString,
                           xmin=dtm.date2num(df.Time_SameDate2), 
                           xmax=dtm.date2num(df.EndTime_SameDate2), 
                           linewidth=self.menuWidget.hlineWidth, 
                           color=df['Resource'].map(self.colors))

        
        #Make own legend: https://stackoverflow.com/questions/39500265/manually-add-legend-items-python-matplotlib
        #red_patch=mpatches.Patch(color='red', label='Sleep')
        sleep_patch=mpatches.Patch(color=self.colors["Sleep"], label='Sleep')
        nursing_patch=mpatches.Patch(color=self.colors["Nursing"], label='Nursing')
        diaper_patch=mpatches.Patch(color=self.colors["Wet"], label='Diaper')
        #bottle_patch=mpatches.Patch(color=self.colors["BottleFormula"], label='Bottle')
        eat_patch=mpatches.Patch(color=self.colors["Eat"], label='Eat')
        work_patch=mpatches.Patch(color=self.colors["Work"], label='Personal')

        
        #self.ax.legend(handles=[sleep_patch,nursing_patch, diaper_patch, eat_patch, work_patch], bbox_to_anchor=(0., -.1, 1, .102), loc=3,
        #plt.legend(handles=[sleep_patch, nursing_patch, diaper_patch, eat_patch, work_patch], bbox_to_anchor=(0., 1.02, 1, .102), loc=3,
        #           ncol=5, mode="expand", borderaxespad=0.) #bbox_to_anchor=(0.9, 0.3)
        if hasattr(self, "_legend") and self._legend is not None:
            self._legend.remove()
            self._legend = None

        self._legend = self.fig.legend(handles=[sleep_patch, nursing_patch, diaper_patch, eat_patch, work_patch],
                                       loc="lower center",
                                       bbox_to_anchor=(0.5, 0.01),
                                       bbox_transform=self.fig.transFigure,
                                       ncol=5,
                                       borderaxespad=0.)
        #plt.legend(handles=[sleep_patch, nursing_patch, diaper_patch, bottle_patch], bbox_to_anchor=(1.05, 1))
        #plt.margins(.15)  #So xticks start at 12:00am
        self.ax.tick_params(axis="x", labelrotation=90, pad=-3)
        #self.ax.tick_params(axis="x", labelrotation=90, pad=-18)
        self.ax.invert_yaxis()
        self.fig.subplots_adjust(left=0.16, right=0.99, top=0.85, bottom=0.30)
        #plt.subplots_adjust(bottom=0.19, top=0.92)
        #plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
        #plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True
        #plt.show()
        #plt.ion()
        #plt.draw()
        
        #self.ax.plot()

        #https://stackoverflow.com/questions/4098131/how-to-update-a-plot-in-matplotlib
        if hasattr(self, "canvas"):
            self.canvas.draw_idle()
        else:
            self.fig.canvas.draw()
            self.fig.canvas.flush_events()

    def resize(self, event):
        self.fig.subplots_adjust(left=0.16, right=0.99, top=0.92, bottom=0.30)
        self.canvas.draw_idle()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Graph")
    app = Page(parent=root, startDate="2017-9-10", endDate="2017-9-25")  #This is to test the pageEngineer
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    app.grid(row=0, column=0, sticky="NESW")
    #w=1000
    #h=650
    #x=1040
    #y=700
    #root.geometry('%dx%d+%d+%d' % (w,h,x,y)) #Position window
    root.protocol("WM_DELETE_WINDOW",app.onClose)
    #root.bind("<Configure>", app.resize) # Resize is handled by the canvas widget's <Configure> binding

    while True:
        root.update_idletasks()
        root.update()  #This blocks

        if app.menuWidget.needToUpdateGraphFlag == 1:
            app.updateGraph(startDate=app.menuWidget.newGraphStartDate,
                            endDate=app.menuWidget.newGraphEndDate)
            app.menuWidget.needToUpdateGraphFlag = 0 #reset flag
