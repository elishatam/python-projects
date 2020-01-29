import tkinter as tk  # python 3
# import Tkinter as tk  # python 2
# https://stackoverflow.com/questions/3085696/adding-a-scrollbar-to-a-group-of-widgets-in-tkinter
# https://stackoverflow.com/questions/7113937/how-do-you-create-a-labelframe-with-a-scrollbar-in-tkinter

class Example(tk.Frame):
    def __init__(self, root):
        '''
        1) Create a canvas widget (C).
        2) Associate a scrollbar with this C
        3) Embed Frame (F) into C
        4) Determine the width and height of F. Put width and height into C's scrollregion.
           This is so the scrollregion exactly matches the size of F
        5) Populate label widgets into F
        
        '''

        tk.Frame.__init__(self, root)
        #1) Create a canvas widget (C).
        self.canvas = tk.Canvas(root, borderwidth=0, background="#ffffff")
        self.frame = tk.Frame(self.canvas, background="#ffffff")
        #2) Associate a scrollbar with this C
        self.vsb = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        #self.vsb.pack(side="right", fill="y")
        self.vsb.grid(row=0, column=1, sticky="NSE")
        #self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.grid(row=0, column=0, sticky="NSWE")
        #self.canvas.grid_columnconfigure(1, weight=1)
        #self.canvas.grid_rowconfigure(0, weight=1)
        #self.vsb.grid_columnconfigure(1, weight=1)
        #self.vsb.grid_rowconfigure(0, weight=1)
        #3) Embed Frame (F) into C
        self.canvas.create_window((4,4), window=self.frame, anchor="nw", 
                                  tags="self.frame")

        #4) Determine the width and height of F. Put width and height into C's scrollregion.
        self.frame.bind("<Configure>", self.onFrameConfigure)

        #5) Populate label widgets into F
        self.populate()

    def populate(self):
        '''Put in some fake data'''
        for row in range(100):
            tk.Label(self.frame, text="%s" % row, width=3, borderwidth="1", 
                     relief="solid").grid(row=row, column=0)
            t="this is the second column for row %s" %row
            tk.Label(self.frame, text=t).grid(row=row, column=1)

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

if __name__ == "__main__":
    root=tk.Tk()
    #Example(root).pack(side="top", fill="both", expand=True)
    Example(root).grid(row=0, column=0, sticky="NSWE")
    #Add this in the expand
    #In grid, any extra space in the parent is allocated proportional
    #to the weight of the row and column
    #By default rows and column have weight=0, so no
    #extra space is given to them.
    #root.grid_columnconfigure(1, weight=1)
    root.grid_rowconfigure(0, weight=1)
    
    root.mainloop()