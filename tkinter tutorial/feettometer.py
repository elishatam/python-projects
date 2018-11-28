#from tkinter import *
import tkinter as tk
from tkinter import ttk, Frame

#https://tkdocs.com/tutorial/firstexample.html

#Will be called when user presses Calculate button or hits Return key
def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

root = tk.Tk()
root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=("N,W,E,S"))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = tk.StringVar()
meters = tk.StringVar()
meters.set(0)          #Set default value

#global variable "feet" is the textvariable of the entry.
#Meaning anytime the entry changes, Tk will automatically update the global variable feet.
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=("W,E"))
#sticky = how the widget would line up within the grid cell

#If we explicitly change the value of a textvariable associated with a widget, the widget will
#automatically be updated with the current contents of the variable
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=("W,E"))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky="W")

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky="W")
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky="E")
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky="W")

#Adds padding around each widget
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
#Cursor will start in this field
feet_entry.focus()
root.bind('<Return>', calculate) #if use presses Return key anywhere within the root window,
                                 # it should call our calculate routine

#Tells Tk to enter its event loop. Needed to make everything run
root.mainloop()


