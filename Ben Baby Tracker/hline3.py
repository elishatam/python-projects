from datetime import datetime, date
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dtm

#https://jakevdp.github.io/PythonDataScienceHandbook/03.11-working-with-time-series.html

df = pd.read_csv('BenjaminErlien_nursing_gantt_short.csv')
#df1 = df1.assign(EndTime=p.Series(df.Time + pd.to_timedelta(df.TotalDuration, unit='m')))
#print(df.Time)
#df.Time = pd.to_datetime(df.Time).astype(datetime)
#Pandas to_datetime() converts string Date time into Python date time object
df.Time = pd.to_datetime(df.Time)  #dtype: datetime64[ns]. Matplotlib can't plot this datatype
'''
df['TOnly'] = df['Time'].dt.time   #object
df['DOnly'] = df['Time'].dt.date   #object
df['DOnly2'] = df['Time'].dt.normalize() #retains datetime64. https://stackoverflow.com/questions/35595710/splitting-timestamp-column-into-seperate-date-and-time-columns
df['EndTime'] = df.Time + pd.to_timedelta(df.TotalDuration, unit='m')
df['EndTimeTOnly'] = df['EndTime'].dt.time
df['DateString'] = df['DOnly'].astype('|S') #https://stackoverflow.com/questions/33957720/how-to-convert-column-with-dtype-as-object-to-string-in-pandas-dataframe
#df['test'] = datetime.combine(date.today(), df['TOnly']) #https://stackoverflow.com/questions/656297/python-time-timedelta-equivalent

df.info()
df
print(df)

#print(dt.date2num(df.Time)) #doesn't work
#print(df.Time.astype(datetime))
df.Time = df.Time.astype(datetime) #Need to change dtype to datetime.date instances
									#https://matplotlib.org/gallery/recipes/common_date_problems.html
df.EndTime = df.EndTime.astype(datetime)
#df.TimeOnly = df.TimeOnly.astype(datetime)
df.TOnly = df.TOnly.astype(datetime)
'''

df['A'] = pd.period_range('2019-01', periods=18, freq='H')
df['B'] = df.Time.strftime('%A')
df.info()
df
print(df)
'''

fig = plt.figure()
ax = fig.add_subplot(111)
ax = ax.xaxis_date()   #Change format later: https://stackoverflow.com/questions/14946371/editing-the-date-formatting-of-x-axis-tick-labels-in-matplotlib
#ax = plt.hlines(df.Number, dt.date2num(df.Time), dt.date2num(df.endtime), linewidth=15, color=df.color)
#ax = plt.hlines(df.Number, dt.date2num(df.Time), dt.date2num(df.endtime), linewidth=15, color=colors[(df.resource)])
#ax = plt.hlines(df.Number, dt.date2num(df.Time), dt.date2num(df.endtime), linewidth=15, color=colors['Sleep'])
#ax = plt.hlines(df.Baby, dt.date2num(df.Time), df.EndTime, linewidth=15, color="red")
#ax = plt.hlines(df.Baby, df.Time, df.EndTime, linewidth=15, color="red")
#dt.date2num = Convert datetime objects to Matplotlib dates.
#ax = plt.hlines(df.Baby, dt.date2num(df.Time), dt.date2num(df.EndTime), linewidth=15, color="red")
ax = plt.hlines(df.DateString, dtm.date2num(df.Time), dtm.date2num(df.EndTime), linewidth=15, color="red")

plt.show()
'''