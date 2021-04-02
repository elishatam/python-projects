#https://stackoverflow.com/questions/28419763/expand-text-widget-to-fill-the-entire-parent-frame-in-tkinter
import tkinter as tk
root = tk.Tk()

input_text_area = tk.Text(root)
input_text_area.grid(row=1, column=0, columnspan=4, sticky="NSWE")
input_text_area.configure(background='#4D4D4D')

#Add this in the expand
#In grid, any extra space in the parent is allocated proportional
#to the weight of the row and column
#By default rows and column have weight=0, so no
#extra space is given to them.
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)

root.mainloop()
