from datetime import datetime, date
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dtm

df = pd.read_csv('BenjaminErlien_nursing_gantt_short.csv')
#df1 = df1.assign(EndTime=p.Series(df.Time + pd.to_timedelta(df.TotalDuration, unit='m')))
#print(df.Time)
#df.Time = pd.to_datetime(df.Time).astype(datetime)
#Pandas to_datetime() converts string Date time into Python date time object
df.Time = pd.to_datetime(df.Time)  #dtype: datetime64[ns]. Matplotlib can't plot this datatype
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


#print(df.Time)
#.to_timedelta converts the entire series into a timedelta object
#to add TotalDuration to Time, both series need to be in datetime and timedelta formats
#df.EndTime = df.Time + pd.to_timedelta(df.TotalDuration, unit='m')
'''
#Make new columns 
df['EndTime'] = df.Time + pd.to_timedelta(df.TotalDuration, unit='m')
df['Date'] = df['Time'].dt.date #https://stackoverflow.com/questions/16176996/keep-only-date-part-when-using-pandas-to-datetime
df['TimeOnly'] = df['Time'].dt.time
df['DateString'] = df['Date'].astype('|S') #https://stackoverflow.com/questions/33957720/how-to-convert-column-with-dtype-as-object-to-string-in-pandas-dataframe
#df['EndTime_TimeOnly'] = df.TimeOnly + pd.to_timedelta(df.TotalDuration, unit='m')
#df['TimeOnly2'] = pd.to_timedelta(pd.to_datetime(df.TimeOnly).dt.strftime('%H:%M:%S'))

df['new_date'] = [d.date() for d in df['Time']] #https://stackoverflow.com/questions/35595710/splitting-timestamp-column-into-seperate-date-and-time-columns
df['new_time'] = [d.time() for d in df['Time']]
df['new_time2'] = df['new_time'] + pd.Timedelta(minutes=2)
#print(df['DateString'])
print(df['Time'])
print(df['Date'])
print(df['TimeOnly'])
print(df['new_date'])
print(df['new_time'])

#print(df['EndTime_TimeOnly'])
#print(df)

#df.TimeOnly = pd.to_datetime(df.TimeOnly)
#print(df.TimeOnly)
#https://stackoverflow.com/questions/29370057/select-dataframe-rows-between-two-dates
#mask = (df['Time'] > '2017-08-02 17:00:00') & (df['Time'] <= '2017-08-03')
#print(df.loc[mask])
#print(df.Time)
'''


#print(dt.date2num(df.Time)) #doesn't work
#print(df.Time.astype(datetime))
df.Time = df.Time.astype(datetime) #Need to change dtype to datetime.date instances
									#https://matplotlib.org/gallery/recipes/common_date_problems.html
df.EndTime = df.EndTime.astype(datetime)
#df.TimeOnly = df.TimeOnly.astype(datetime)
df.TOnly = df.TOnly.astype(datetime)

print(df.Time)

df.info()
df
#df[df.Time]


fig = plt.figure()
ax = fig.add_subplot(111)
ax = ax.xaxis_date()
#ax = plt.hlines(df.Number, dt.date2num(df.Time), dt.date2num(df.endtime), linewidth=15, color=df.color)
#ax = plt.hlines(df.Number, dt.date2num(df.Time), dt.date2num(df.endtime), linewidth=15, color=colors[(df.resource)])
#ax = plt.hlines(df.Number, dt.date2num(df.Time), dt.date2num(df.endtime), linewidth=15, color=colors['Sleep'])
#ax = plt.hlines(df.Baby, dt.date2num(df.Time), df.EndTime, linewidth=15, color="red")
#ax = plt.hlines(df.Baby, df.Time, df.EndTime, linewidth=15, color="red")
#dt.date2num = Convert datetime objects to Matplotlib dates.
#ax = plt.hlines(df.Baby, dt.date2num(df.Time), dt.date2num(df.EndTime), linewidth=15, color="red")
ax = plt.hlines(df.DateString, dtm.date2num(df.Time), dtm.date2num(df.EndTime), linewidth=15, color="red")

plt.show()
