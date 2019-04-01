from tkinter import *
from tkinter import ttk
import gclib

g=gclib.py() #make an instance of the gclib python class
print('gclib version:', g.GVersion())
g.GOpen('169.254.168.101 --direct -s ALL')
print(g.GInfo())

#--------Definitions-----
def enter_term_command(*args):
    try:
        g.GCommand(term_command.get())
    except ValueError:
        pass

def beginE(*args):
    try:
        #g.GCommand('BGE')
        value = float(pr.get())
    except ValueError:
        pass

def setpr(*args):
    try:
        #g.GCommand('PRE=')
        value = float(pr.get())
        g.GCommand('PRE=' + repr(value))
        pr_value.set(value)
    except ValueError:
        pass

#---------MAIN--------------
root = Tk()
root.title("Test Motors")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

pr = StringVar()
pr_value = StringVar()
term_command = StringVar()

pr_entry = ttk.Entry(mainframe, width=7, textvariable=pr)
pr_entry.grid(column=2, row=2, sticky=(W,E))

ttk.Label(mainframe, text="Set position relative").grid(column=1, row=2, sticky=W)
ttk.Button(mainframe, text="Set PR", command=setpr).grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, textvariable=pr_value).grid(column=4, row=2, sticky=W)

term_command_entry = ttk.Entry(mainframe, width=15, textvariable=term_command)
term_command_entry.grid(column=1, row=1, sticky=(W,E))
ttk.Button(mainframe, text="Enter Command", command=enter_term_command).grid(column=3,row=1, sticky=W)


#Adds padding around each widget
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
#Cursor will start in this field
pr_entry.focus()


#Tells Tk to enter its event loop. Needed to make everything run
root.mainloop()
