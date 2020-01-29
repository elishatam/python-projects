import matplotlib
from matplotlib import pyplot as plt
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np
import tkinter as tk
from tkinter import ttk

class Page(tk.Frame):
    def __init__(self, parent):

        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.fig = plt.figure(1)
        self.fig.set_size_inches(10, 5)
        self.ax = self.fig.add_subplot(111)    

        
        canvas = FigureCanvasTkAgg(self.fig, master=self) #tk.DrawingArea
        #canvas.draw()
        canvas.get_tk_widget().grid(row=1,column=0)

        x = np.linspace(0, 10, 1000)
        self.ax.plot(x, np.sin(x));

        toolbarFrame = tk.Frame(master=root)
        toolbarFrame.grid(row=2,column=0, sticky="W")
        #To use this toolbar with grid, need to put it in its own frame
        toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
        #toolbar.update()

        #self.fig.canvas.draw()
        #plt.show()

    def onClose(self):
        print("closeGraph")
        self.destroy()
        self.parent.destroy()
        #plt.close('all')
        plt.close()

  


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Graph")
    app = Page(parent=root)  #This is to test the pageEngineer
    app.grid(row=0, column=0, sticky="W")
    #w=1000
    #h=650
    #x=1040
    #y=700
    #root.geometry('%dx%d+%d+%d' % (w,h,x,y)) #Position window
    root.protocol("WM_DELETE_WINDOW",app.onClose)

    while True:
        root.update_idletasks()
        root.update()  #This blocks
