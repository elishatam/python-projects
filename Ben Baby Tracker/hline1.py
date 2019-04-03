from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dt

df = pd.read_csv('hline1.csv')
print(df.starttime)

df.starttime = pd.to_datetime(df.starttime).astype(datetime)
df.endtime = pd.to_datetime(df.endtime).astype(datetime)
print(df.starttime)


colors = {
	"Sleep": "red",
	"Nurse": "black",
	"Diaper": "blue"
}


print(dt.date2num(df.starttime))


fig = plt.figure()
ax = fig.add_subplot(111)
ax = ax.xaxis_date()

#This line works
#ax = plt.hlines(df.Number, dt.date2num(df.starttime), dt.date2num(df.endtime), linewidth=15, color=df.color)  #workaround

#This line doesn't work
#I wish I could get this to work where a dictionary could look up what the df.resource (key) is (i.e nurse or sleep)
#and then output the value (correlating color). However when I run this line, I get this error
#TypeError: 'Series' objects are mutable, thus they cannot be hashed
#ax = plt.hlines(df.Number, dt.date2num(df.starttime), dt.date2num(df.endtime), linewidth=15, color=colors[(df.resource)])
ax = plt.hlines(df.Number, dt.date2num(df.starttime), dt.date2num(df.endtime), linewidth=15, color=df['resource'].map(colors))

#This line works
#But when I run the below line with what I think would be the value returned from the key, it works fine.
#ax = plt.hlines(df.Number, dt.date2num(df.starttime), dt.date2num(df.endtime), linewidth=15, color=colors['Sleep'])
plt.show()



'''
https://stackoverflow.com/questions/31820578/how-to-plot-stacked-event-duration-gantt-charts-using-python-pandas
'''