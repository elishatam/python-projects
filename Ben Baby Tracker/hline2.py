from datetime import datetime, date
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dtm

df = pd.read_csv('BenjaminErlien_nursing_gantt_short.csv')

#Pandas to_datetime() converts string Date time into Python date time object
df.Time = pd.to_datetime(df.Time)  #dtype: datetime64[ns]. Matplotlib can't plot this datatype
df['EndTime'] = df.Time + pd.to_timedelta(df.LeftDuration, unit='m') + pd.to_timedelta(df.RightDuration, unit='m')
#df['TimeOnly'] = df['Time'].dt.time   #object
df['DateOnly'] = df['Time'].dt.date   #object
#df['DateOnly2'] = df['Time'].dt.normalize() #retains datetime64. https://stackoverflow.com/questions/35595710/splitting-timestamp-column-into-seperate-date-and-time-columns
#df['EndTimeTOnly'] = df['EndTime'].dt.time

#Make Date a string. Needed for hline y axis
#https://stackoverflow.com/questions/33957720/how-to-convert-column-with-dtype-as-object-to-string-in-pandas-dataframe
df['DateString'] = df['DateOnly'].astype('|S') 

#Make the same dummy date for the date time so hlines will stack
df['Time_SameDate']=df.Time.map(lambda t: t.replace(year=2019, month=1, day=1)) #https://stackoverflow.com/questions/17152719/change-date-of-a-datetimeindex
df['EndTime_SameDate']=df.EndTime.map(lambda t: t.replace(year=2019, month=1, day=1))
#df.info()
#df
#print(df)

#Need to change dtype to datetime.date instances
#https://matplotlib.org/gallery/recipes/common_date_problems.html
#df.Time = df.Time.astype(datetime) 									
#df.EndTime = df.EndTime.astype(datetime)
df.Time_SameDate = df.Time_SameDate.astype(datetime)
df.EndTime_SameDate = df.EndTime_SameDate.astype(datetime)


df.info()
df
print(df)


fig = plt.figure()
ax = fig.add_subplot(111)
ax.xaxis.set_major_formatter(dtm.DateFormatter('%I:%M %p'))
ax.xaxis.set_major_locator(dtm.HourLocator(byhour=range(0,24,4)))



#myFmt = dtm.DateFormatter('%H:%M')
#ax = ax.xaxis.set_major_formatter(myFmt)
#ax = ax.xaxis_date()   #Change format later: https://stackoverflow.com/questions/14946371/editing-the-date-formatting-of-x-axis-tick-labels-in-matplotlib
#ax = plt.hlines(df.Number, dt.date2num(df.Time), dt.date2num(df.endtime), linewidth=15, color=df.color)
#ax = plt.hlines(df.Number, dt.date2num(df.Time), dt.date2num(df.endtime), linewidth=15, color=colors[(df.resource)])
#ax = plt.hlines(df.Number, dt.date2num(df.Time), dt.date2num(df.endtime), linewidth=15, color=colors['Sleep'])
ax = plt.hlines(df.DateString, dtm.date2num(df.Time_SameDate), dtm.date2num(df.EndTime_SameDate), linewidth=15, color="red")

plt.margins(.15)  #So xticks start at 12:00am
plt.xticks(rotation=90)
fig.tight_layout()  #Border will fit around axis
plt.show()
