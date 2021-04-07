import tkinter as tk
from tkinter import ttk
import pandas as pd

#
class daysWidget(tk.Frame):
    def __init__(self, parent, obj_days_forGraph):
        tk.Frame.__init__(self, parent)
        
        #initialize values that are used across modules
        self.needToUpdateGraphFlag = 0
        self.hlineWidth=8

        self.daysFrame = ttk.Labelframe(self, text=("Days"))
        self.daysFrame.grid(row=0, column=0, sticky="NSW",
            padx=5, pady=2)

        self.updateChart(obj_days_forGraph=obj_days_forGraph)
            
        '''
        labelStartDate = tk.Label(menuFrame, text="Start Date")
        labelStartDate.grid(row=0, column=0, sticky='W,E', padx=5, pady=2)

        self.startDateValue = tk.StringVar(value=initStartDate)
        startDateEntry = ttk.Entry(menuFrame, textvariable=self.startDateValue, 
            width=20)
        startDateEntry.grid(row=0, column=1, sticky="W,E", padx=5, pady=2)

        labelEndDate = tk.Label(menuFrame, text="End Date")
        labelEndDate.grid(row=1, column=0, sticky='W,E', padx=5, pady=2)
        self.endDateValue = tk.StringVar(value=initEndDate)
        endDateEntry = ttk.Entry(menuFrame, textvariable=self.endDateValue, 
            width=20)
        endDateEntry.grid(row=1, column=1, sticky="W,E", padx=5, pady=2)

        #Button to update graph
        self.btnUpdateGraph = tk.Button(menuFrame, text="Update Graph",
            command=lambda: self.needToUpdateGraph(startDate=self.startDateValue.get(),
                                            endDate=self.endDateValue.get())
            )
        self.btnUpdateGraph.grid(row=1, column=2, sticky="W")
        '''

    def updateChart(self, obj_days_forGraph):
                # take the data
        lst = obj_days_forGraph  #This is a list of objects.
                                    #How to change the objects to tuples

        print(lst)
        #print(len(lst))
        #This is a list of tuples.
        #A tuple stores multiple items in a single variable.
        #lst = [(1,'Raj','Mumbai',19),
        #       (2,'Aaryan','Pune',18),
        #       (3,'Vaishnavi','Mumbai',20),
        #       (4,'Rachna','Mumbai',21),
        #       (5,'Shubham','Delhi',21)]

                   
        # find total number of rows and
        # columns in list
        total_rows = len(lst)
        #total_columns = len(lst[0])
        total_columns = 6

        #Label Header
        self.e = ttk.Entry(self.daysFrame, width=20)
        self.e.grid(row=0, column=0)
        self.e.insert(tk.END, "Time0 of longest stretch")

        self.e = ttk.Entry(self.daysFrame, width=15)
        self.e.grid(row=0, column=1)
        self.e.insert(tk.END, "# Night Feeds")

        self.e = ttk.Entry(self.daysFrame, width=15)
        self.e.grid(row=0, column=2)
        self.e.insert(tk.END, "# Night Wakes")

        self.e = ttk.Entry(self.daysFrame, width=15)
        self.e.grid(row=0, column=3)
        self.e.insert(tk.END, "Time Btwn Feeds")

        #https://www.geeksforgeeks.org/create-table-using-tkinter/
        #create a table
        for i in range(total_rows):
            #for j in range(total_columns):
            #    self.e = ttk.Entry(daysFrame, width=20)
            #    self.e.grid(row=i, column=j)
            #    self.e.insert(tk.END, lst[i][j])    #END indicates that the data continues to append
                                                    #at the end of previous data in the Entry widget
        
            self.e = ttk.Entry(self.daysFrame, width=20)
            self.e.grid(row=i+1, column=0)
            self.e.insert(tk.END, lst[i].longestTimeBtwnFeeds_T0)

            self.e = ttk.Entry(self.daysFrame, width=15)
            self.e.grid(row=i+1, column=1)
            self.e.insert(tk.END, lst[i].numOfNightFeeds)

            self.e = ttk.Entry(self.daysFrame, width=15)
            self.e.grid(row=i+1, column=2)
            self.e.insert(tk.END, lst[i].numOfNightWakes)

            longestTimeBetweenFeeds_hr = lst[i].longestTimeBtwnFeeds // 60
            longestTimeBetweenFeeds_min = lst[i].longestTimeBtwnFeeds % 60

            self.e = ttk.Entry(self.daysFrame, width=15)
            self.e.grid(row=i+1, column=3)
            self.e.insert(tk.END, str(int(longestTimeBetweenFeeds_hr)) + "hr " + str(int(longestTimeBetweenFeeds_min))+"min")  



    def needToUpdateGraph(self, startDate, endDate):
        self.needToUpdateGraphFlag = 1
        self.newGraphStartDate = startDate
        self.newGraphEndDate = endDate

        #update entry dates
        self.startDateValue.set(startDate)
        self.endDateValue.set(endDate)

        #update hline width if > 60 days
        dayDifference = pd.to_datetime(endDate) - pd.to_datetime(startDate)
        if dayDifference.days > 60:
            print("update width to 2")
            self.hlineWidth = 1
        else:
            print("update width to 8")
            self.hlineWidth = 8

    def offsetDateByMonth_Str(self, date_dateTime, numberOfMonths):
        newDate=str((date_dateTime + pd.DateOffset(months=numberOfMonths)).date())
        return newDate
