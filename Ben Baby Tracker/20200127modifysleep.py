from datetime import datetime, date
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dtm
import matplotlib.patches as mpatches
import time

df = pd.read_csv('1to6month.csv')
df.Time = pd.to_datetime(df.Time)  #dtype: datetime64[ns]. Matplotlib can't plot this datatype

# Select observations between two datetimes
#df[(df['date'] > '2002-1-1 01:00:00') & (df['date'] <= '2002-1-1 04:00:00')]
#df[(df.Time > "2017-10-10 00:00:00")]
#df[(df['Time'] > pd.to_datetime(["2017-10-10 00:00:00"]))]
mask = (df.Time > "2017-12-1") & (df.Time < "2018-1-01")
df = df.loc[mask]
df = df.sort_index().reset_index(drop=True)
print(df)
#--------------
#Create new DF. https://thispointer.com/python-pandas-how-to-add-rows-in-a-dataframe-using-dataframe-append-loc-iloc/
#df = df0.append({'Time' : '2017-10-11 0:00:00', 'TotalDuration': '10'}, ignore_index=True) 
#df.Time = pd.to_datetime(df.Time)

#print(df)
#df.info()
#print(df)
#Find indexes of last row of day
#compareDate = pd.to_datetime(["2017-08-02 20:00:00"])
#timestring = "20:00:00"
#df[df['Time'].dt.time > time.strptime(timestring, "%H:%M:%S")]
#Insert a new row after last row of day
#Modify last row of day to end at midnight
#In new row, start at midnight and end

#Pandas to_datetime() converts string Date time into Python date time object
#df.Time = pd.to_datetime(df.Time)  #dtype: datetime64[ns]. Matplotlib can't plot this datatype
df['EndTime'] = df.Time + pd.to_timedelta(df.TotalDuration, unit='m')
#df['TimeOnly'] = df['Time'].dt.time   #object
df['DateOnly'] = df['Time'].dt.date   #object
#df['DateOnly2'] = df['Time'].dt.normalize() #retains datetime64. https://stackoverflow.com/questions/35595710/splitting-timestamp-column-into-seperate-date-and-time-columns
#df['EndTimeTOnly'] = df['EndTime'].dt.time

#Make Date a string. Needed for hline y axis
#https://stackoverflow.com/questions/33957720/how-to-convert-column-with-dtype-as-object-to-string-in-pandas-dataframe
df['DateString'] = df['DateOnly'].astype('|S').apply(lambda s: s.decode('utf-8'))
#The 'b' prefix indicates a Python 3 bytes literal that represents an object rather than an unicode string. So if you want to remove the prefix you could decode the bytes object using the string decode method before saving it to a csv file:

#Make the same dummy date for the date time so hlines will stack
df['Time_SameDate']=df.Time.map(lambda t: t.replace(year=2019, month=1, day=1)) #https://stackoverflow.com/questions/17152719/change-date-of-a-datetimeindex
df['EndTime_SameDate']=df.EndTime.map(lambda t: t.replace(year=2019, month=1, day=1))

df['Daydifference']=df.DateOnly - date(2017,8,2)
#for index, row in df.iterrows():
#	df['Time_SameDate2']=df.Time - pd.to_timedelta('1 days')
#Make all the dates the same day of 8/2/2017
df['Time_SameDate2']=df.Time - df.Daydifference
df['EndTime_SameDate2']=df.EndTime - df.Daydifference
#df.info()
#df
#print(df)
print(df)
#Find indexes of dates after this time - when Ben fell asleep after 6:40pm and woke up after midnight
compareStartDate = pd.to_datetime(["2017-08-02 18:40:00"])
compareEndDate = pd.to_datetime(["2017-08-03 00:10:00"])
midnight_indices = (df[((df["Time_SameDate2"] > compareStartDate[0]) & (df["EndTime_SameDate2"]>compareEndDate[0]))].index.values) #https://stackoverflow.com/questions/18327624/find-elements-index-in-pandas-series
																#https://stackoverflow.com/questions/17241004/how-do-i-get-a-dataframe-index-series-column-as-an-array-or-list
#midnight_indices = [0]
print(midnight_indices)



#Insert a new row after these indices. Make EndTime of new row the same as EndTime of indexA
for indexA in midnight_indices:
	#https://stackoverflow.com/questions/15888648/is-it-possible-to-insert-a-row-at-an-arbitrary-position-in-a-dataframe-using-pan?rq=1
	#line = pd.DataFrame({'Time_SameDate2': pd.to_datetime(["2017-08-02 00:00:00"]), 'EndTime_SameDate2': df.EndTime_SameDate2[indexA] - pd.Timedelta(days=1), 'DateString': df.DateString[indexA+1], 'Resource': 'Sleep'}, index=[indexA+0.5])
	#line = pd.DataFrame({'Time_SameDate2': pd.to_datetime(["2017-08-02 00:00:00"]), 'EndTime_SameDate2': df.EndTime_SameDate2[indexA] - pd.Timedelta(days=1), 'DateString': df.DateString[indexA+1], 'Resource': 'Sleep'}, index=[indexA+0.5])
	line = pd.DataFrame({'Time_SameDate2': pd.to_datetime(["2017-08-02 00:00:00"]), 'EndTime_SameDate2': df.EndTime_SameDate2[indexA] - pd.Timedelta(days=1), 'DateString': df.DateString[indexA+1], 'Resource': 'Sleep'}, index=[indexA+0.5])
	df = df.append(line, ignore_index=False)

#indexA = 230
#line = pd.DataFrame({'Time_SameDate2': pd.to_datetime(["2017-08-02 00:00:00"]), 'EndTime_SameDate2': df.EndTime_SameDate2[indexA] - pd.Timedelta(days=1), 'DateString': df.DateString[indexA+1], 'Resource': 'Sleep'}, index=[indexA+0.5])
#df = df.append(line, ignore_index=False)
#print(df.EndTime_SameDate2[indexA] - pd.Timedelta(days=1))
#print(df.DateString[indexA+1])
#print([indexA+0.5])

#Move EndTime_SameDate2 to midnight. 
for indexA in midnight_indices:
	df.iloc[indexA, df.columns.get_loc('EndTime_SameDate2')] = pd.to_datetime(["2017-08-03 00:00:00"])

#df.iloc[indexA, df.columns.get_loc('EndTime_SameDate2')] = pd.to_datetime(["2017-08-03 00:00:00"])	
df = df.sort_index().reset_index(drop=True)

#print(df)

#Need to change dtype to datetime.date instances
#https://matplotlib.org/gallery/recipes/common_date_problems.html
#df.Time = df.Time.astype(datetime) 									
#df.EndTime = df.EndTime.astype(datetime)
df.Time_SameDate = df.Time_SameDate.astype(datetime)
df.EndTime_SameDate = df.EndTime_SameDate.astype(datetime)
df.Time_SameDate2 = df.Time_SameDate2.astype(datetime)
df.EndTime_SameDate2 = df.EndTime_SameDate2.astype(datetime)

df.info()
df
#print(df)

#print(df.DateString)
#print(df.Time_SameDate2)
#print(df.EndTime_SameDate2)


#print(pd.to_datetime(["2017-08-02 20:00:00"]))
#compareDate = pd.to_datetime(["2017-08-02 20:00:00"])

#https://stackoverflow.com/questions/34586069/valueerror-series-lengths-must-match-to-compare-when-matching-dates-in-pandas
#mask = (df['Time_SameDate2'] < compareDate[0])
#df  = df.loc[mask]
#print(df)

#print(df.mask(mask))
#print(df.where(mask,10))



#if df['Time_SameDate2'] > compareDate[0]:
#	print(df.Time_SameDate2)

#fig = plt.figure(figsize=(5,5))
fig = plt.figure()
ax = fig.add_subplot(111)
ax.xaxis.set_major_formatter(dtm.DateFormatter('%I:%M %p'))
ax.xaxis.set_major_locator(dtm.HourLocator(byhour=range(0,24,4)))
ax.xaxis.set_minor_locator(dtm.HourLocator(byhour=range(0,24,1)))
ax.xaxis.tick_top()
ax.xaxis.set_label_position('top')

colors = {
	'Sleep': '#cdc8b1',
	'Nursing': '#ff8c00',
	'Wet': '#00bfff',
	'Dirty': '#00bfff',
	'Mixed': '#00bfff',
	'Dry': '#00bfff',
	'BottleFormula': '#ffffff',
	'BottlePumped': '#ff8c00',
	'Eat': '#F3050D',
	'Work': '#7fff00'
}

#ax = plt.hlines(df.DateString, dtm.date2num(df.Time_SameDate2), dtm.date2num(df.EndTime_SameDate2), linewidth=15, color=df['Resource'].map(colors))
ax = plt.hlines(df.DateString, dtm.date2num(df.Time_SameDate2), dtm.date2num(df.EndTime_SameDate2), linewidth=8, color=df['Resource'].map(colors))

#Make own legend: https://stackoverflow.com/questions/39500265/manually-add-legend-items-python-matplotlib
#red_patch=mpatches.Patch(color='red', label='Sleep')
sleep_patch=mpatches.Patch(color=colors["Sleep"], label='Sleep')
nursing_patch=mpatches.Patch(color=colors["Nursing"], label='Nursing')
diaper_patch=mpatches.Patch(color=colors["Wet"], label='Diaper')
bottle_patch=mpatches.Patch(color=colors["BottleFormula"], label='Bottle')
eat_patch=mpatches.Patch(color=colors["Eat"], label='Eat')
work_patch=mpatches.Patch(color=colors["Work"], label='Personal')

plt.legend(handles=[sleep_patch,nursing_patch, diaper_patch, eat_patch, work_patch], bbox_to_anchor=(0., -.1, 1, .102), loc=3,
#plt.legend(handles=[sleep_patch, nursing_patch, diaper_patch, eat_patch, work_patch], bbox_to_anchor=(0., 1.02, 1, .102), loc=3,
           ncol=5, mode="expand", borderaxespad=0.) #bbox_to_anchor=(0.9, 0.3)
#plt.legend(handles=[sleep_patch, nursing_patch, diaper_patch, bottle_patch], bbox_to_anchor=(1.05, 1))
#plt.margins(.15)  #So xticks start at 12:00am
plt.xticks(rotation=90)
fig.tight_layout()  #Border will fit around axis
plt.gca().invert_yaxis()
plt.subplots_adjust(bottom=0.13)
#plt.subplots_adjust(bottom=0.19, top=0.92)
#plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
#plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True
plt.show()


