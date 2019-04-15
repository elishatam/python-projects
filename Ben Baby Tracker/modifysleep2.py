from datetime import datetime, date
#import pandas as pd
import matplotlib.pyplot as plt
#import matplotlib.dates as dtm
#import matplotlib.patches as mpatches

filename = "month3_pythonmod.csv"
plt.figure()

# read all lines into list of strings
with open(filename, 'r') as f:
    content = f.readlines()[1:]

content = [x.strip() for x in content]

#Converts to long array
dates = []
for line in content:
    splt = line.split(',')
    dates.append(datetime.strptime(splt[1], ' %I:%M %p"').time())

print(content)
'''
df = pd.read_csv('month3_pythonmod.csv')

#Pandas to_datetime() converts string Date time into Python date time object
df.Time = pd.to_datetime(df.Time)  #dtype: datetime64[ns]. Matplotlib can't plot this datatype
df['EndTime'] = df.Time + pd.to_timedelta(df.TotalDuration, unit='m')
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

df['Daydifference']=df.DateOnly - date(2017,8,2)
#for index, row in df.iterrows():
#	df['Time_SameDate2']=df.Time - pd.to_timedelta('1 days')
df['Time_SameDate2']=df.Time - df.Daydifference
df['EndTime_SameDate2']=df.EndTime - df.Daydifference
#df.info()
#df
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
print(df)


#print(pd.to_datetime(["2017-08-02 20:00:00"]))
compareDate = pd.to_datetime(["2017-08-02 20:00:00"])

#https://stackoverflow.com/questions/34586069/valueerror-series-lengths-must-match-to-compare-when-matching-dates-in-pandas
mask = (df['Time_SameDate2'] < compareDate[0])
#df  = df.loc[mask]
#print(df)

#print(df.mask(mask))
print(df.where(mask,10))

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
'''
