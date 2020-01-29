import tkinter as tk
from tkinter import ttk
import pandas as pd

class menuWidget(tk.Frame):
    def __init__(self, parent, initStartDate, initEndDate, originalDataFirstDate,
        originalDataLastDate):
        tk.Frame.__init__(self, parent)
        
        self.needToUpdateGraphFlag = 0

        menuFrame = ttk.Labelframe(self, text=("Menu"))
        menuFrame.grid(row=0, column=0, sticky="NSW",
            padx=5, pady=2)

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

        btnFrame = ttk.Labelframe(self, text=("Set Time Periods"))
        btnFrame.grid(row=0, column=1, sticky="NSW",
            padx=5, pady=2)
        self.button=[]
        btnNameList=["2 Weeks", "Month 1", "Month 2", "Month 3", "Month 4", 
                    "Month 5", "Month 6", "Full"]
        startDateList=[self.offsetDateByMonth_Str(originalDataFirstDate,0),
                        self.offsetDateByMonth_Str(originalDataFirstDate,0),
                        self.offsetDateByMonth_Str(originalDataFirstDate,1),
                        self.offsetDateByMonth_Str(originalDataFirstDate,2),
                        self.offsetDateByMonth_Str(originalDataFirstDate,3),
                        self.offsetDateByMonth_Str(originalDataFirstDate,4),
                        self.offsetDateByMonth_Str(originalDataFirstDate,5),
                        self.offsetDateByMonth_Str(originalDataFirstDate,0),
                        ]
        endDateList=[str(originalDataFirstDate+pd.Timedelta(days=14)),
                    self.offsetDateByMonth_Str(originalDataFirstDate,1),
                    self.offsetDateByMonth_Str(originalDataFirstDate,2),
                    self.offsetDateByMonth_Str(originalDataFirstDate,3), 
                    self.offsetDateByMonth_Str(originalDataFirstDate,4),
                    self.offsetDateByMonth_Str(originalDataFirstDate,5), 
                    self.offsetDateByMonth_Str(originalDataFirstDate,6),
                    str(originalDataLastDate)
                    ]
        rowList=[0,0,0,0,1,1,1,1]
        columnList=[3,4,5,6,3,4,5,6]
        
        for i in range(0,len(btnNameList)):
            #print("i: " + str(i))
            self.button.append(tk.Button(btnFrame,
                    text=btnNameList[i],
                    command=lambda i=i: self.needToUpdateGraph(startDate=startDateList[i],
                    endDate=endDateList[i])))
            self.button[i].grid(row=rowList[i], column=columnList[i], sticky="WE")

    def needToUpdateGraph(self, startDate, endDate):
        self.needToUpdateGraphFlag = 1
        self.newGraphStartDate = startDate
        self.newGraphEndDate = endDate

        #update entry dates
        self.startDateValue.set(startDate)
        self.endDateValue.set(endDate)

    def offsetDateByMonth_Str(self, date_dateTime, numberOfMonths):
        newDate=str((date_dateTime + pd.DateOffset(months=numberOfMonths)).date())
        return newDate
