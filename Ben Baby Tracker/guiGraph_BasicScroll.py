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
        #self.fig.set_size_inches(10, 5)
        self.ax = self.fig.add_subplot(111)    
        x = np.linspace(0, 10, 1000)
        self.ax.plot(x, np.sin(x));
        
        #self.canvas = FigureCanvasTkAgg(self.fig, master=self) #tk.DrawingArea
        #canvas.draw()
        #self.canvas.get_tk_widget().grid(row=0,column=0)

        self.canvas2 = tk.Canvas(parent, width=800, height=400, borderwidth=0, background="#ffffff")
        self.frame = tk.Frame(self.canvas2, background="#ffffff")
        self.vsb = tk.Scrollbar(parent, orient="vertical", command=self.canvas2.yview)
        self.canvas2.configure(yscrollcommand=self.vsb.set)
        self.vsb.grid(row=1, column=1, sticky="NSE")
        self.canvas2.grid(row=1, column=0, sticky="NSWE")
        #3) Embed Frame (F) into C
        self.canvas2.create_window((4,4), window=self.frame, anchor="nw", 
                                  tags="self.frame")
        #4) Determine the width and height of F. Put width and height into C's scrollregion.
        self.frame.bind("<Configure>", self.onFrameConfigure)
        
        self.populate()



        #self.fig.canvas.draw()
        #plt.show()

    def onClose(self):
        print("closeGraph")
        self.destroy()
        self.parent.destroy()
        #plt.close('all')
        plt.close()

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas2.configure(scrollregion=self.canvas2.bbox("all"))  

    def populate(self):
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame) #tk.DrawingArea
        #canvas.draw()
        self.canvas.get_tk_widget().grid(row=0,column=0)        

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
