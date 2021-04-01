import pandas as pd
import time
import numpy as np
from datetime import datetime, date, timedelta
from itertools import cycle

class Data:
    def __init__(self, filename, startDate, endDate):
        self.filename = filename
        self.startDate = startDate
        self.endDate = endDate
        self.prepareData()
        

    def prepareData(self):
        self.df = pd.read_csv(self.filename)
        self.df.Time = pd.to_datetime(self.df.Time) #dtype: datetime64[ns].

        

        originalDF=self.df.sort_values(by='Time').reset_index(drop=True)
        originalFirstTimeValue = originalDF.iloc[0]['Time'] #Access first row as a series with iloc. dateTime value
        self.originalFirstDate = originalFirstTimeValue.date()

        originalLastTimeValue = originalDF.iloc[-1]['Time']
        self.originalLastDate = originalLastTimeValue.date()
               
        self.setDataFrameDateRange(self.startDate, self.endDate)

        
        #print(self.df)
        #Sort dataframe by Time column. Reset the index
        self.df = self.df.sort_values(by='Time').reset_index(drop=True)


        #Create new dataframe for counting
        self.setDFForCounting(self.df)

        #Add a dummy row at the end. Needed for addRowAfterMidnightSleep()
        self.addDummyRowAtEnd()

        if self.startDate == "2017-08-02":
            print("don't add in firstSleepEntry")
        else:
            self.addFirstSleepEntry()

        #Add in necessary columns
        self.df['EndTime'] = self.df.Time + pd.to_timedelta(self.df.TotalDuration, unit='m')
        self.df['DateOnly'] = self.df['Time'].dt.date   #object
        #Make Date a string. Needed for hline y axis
        #https://stackoverflow.com/questions/33957720/how-to-convert-column-with-dtype-as-object-to-string-in-pandas-dataframe
        self.df['DateString'] = self.df['DateOnly'].astype('|S').apply(lambda s: s.decode('utf-8'))
        #The 'b' prefix indicates a Python 3 bytes literal that represents an object rather than an unicode string. So if you want to remove the prefix you could decode the bytes object using the string decode method before saving it to a csv file:

        #Make the same dummy date (1/1/2019) for the date time 
        #so hlines will stack
        self.df['Time_SameDate']=self.df.Time.map(lambda t: t.replace(year=2019, month=1, day=1)) #https://stackoverflow.com/questions/17152719/change-date-of-a-datetimeindex
        self.df['EndTime_SameDate']=self.df.EndTime.map(lambda t: t.replace(year=2019, month=1, day=1))
        self.df['Daydifference']=self.df.DateOnly - date(2017,8,2)
        #Make all the dates the same day (8/2/2017)
        self.df['Time_SameDate2']=self.df.Time - self.df.Daydifference
        self.df['EndTime_SameDate2']=self.df.EndTime - self.df.Daydifference
        self.df['AgeInWeeks']=self.howManyWeeksOld(self.df['DateOnly'])
        
        self.addRowAfterMidnightSleep()

        #Need to change dtype to datetime.date instances
        #https://matplotlib.org/gallery/recipes/common_date_problems.html
        #Not needed of python 3.8. Needed for python 3.4
        #self.df.Time_SameDate = self.df.Time_SameDate.astype(datetime)
        #self.df.EndTime_SameDate = self.df.EndTime_SameDate.astype(datetime)
        #self.df.Time_SameDate2 = self.df.Time_SameDate2.astype(datetime)
        #self.df.EndTime_SameDate2 = self.df.EndTime_SameDate2.astype(datetime)

        #self.df.info()
        #self.df
        #print(len(self.df))
        #print(self.df) 
        #https://www.geeksforgeeks.org/selecting-rows-in-pandas-dataframe-based-on-conditions/
        #create new dataframe of selected rows
        #self.dfDay = self.df[self.df.DateOnly == pd.to_datetime("2017-09-02")]
        #self.dfDay = self.df[self.df.DateOnly == pd.to_datetime(self.startDate)]

        #Get indices of feedings
        #listOfFeedings = self.df.index[(self.df['Resource'] == "Nursing") | (self.df['Resource'] == "BottlePumped") | (self.df['Resource'] == "BottleFormula")].tolist()
        #print(listOfFeedings)
        #self.calculateTimeFromLastFeeding(listOfFeedings)

    def calculateTimeFromLastFeeding(self, listOfFeedings, dataframe):
        #Get next element
        #https://www.kite.com/python/answers/how-to-get-the-next-element-while-cycling-through-a-list-in-python
        myList = cycle(listOfFeedings) #Cycle through the listOFFeedings. myList = iterator
        next(myList)                   #Returns the next item in an iterator

        list_feedings=[]
        df_feeds = pd.DataFrame(columns = ["Time0_Index", "Time0", "Time1_Index", "Time1", "Time Difference"])
        for i in listOfFeedings:
            nextElement = next(myList)  #Gets the next element in the cycle iterator
            timeDifference = (dataframe.iloc[nextElement]['TimeRepeat']-dataframe.iloc[i]['TimeRepeat'])/np.timedelta64(1, 'm')
            list_feedings = [i, dataframe.iloc[i]['TimeRepeat'], nextElement, dataframe.iloc[nextElement]['TimeRepeat'], timeDifference]
            df_feeds_length = len(df_feeds)
            df_feeds.loc[df_feeds_length] = list_feedings
        #print(timeFromLastFeeding)    
        #https://moonbooks.org/Articles/Hot-to-find-the-largest-number-and-its-index-in-a-list-with-python-/
        #print("longest time since last feeding: " + str(max(timeFromLastFeeding)) + " at index: " + str(timeFromLastFeeding.index(max(timeFromLastFeeding))))
        print(df_feeds)
        longestTimeBetweenFeeds = df_feeds["Time Difference"].max()
        index_longestTimeBetweenFeeds = df_feeds["Time Difference"].idxmax()
        time0_longestTime = df_feeds["Time0"][index_longestTimeBetweenFeeds]
        time1_longestTime = df_feeds["Time1"][index_longestTimeBetweenFeeds]
        print("longest time since last feeding (min): " + str(longestTimeBetweenFeeds) + " at index: " + str(index_longestTimeBetweenFeeds) + 
            ". " + str(time0_longestTime) + " and " + str(time1_longestTime))
        
    #https://stackoverflow.com/questions/41311990/python-pandas-differences-between-two-dates-in-weeks
    def howManyWeeksOld(self, date):
        x = pd.to_datetime(date) - pd.to_datetime("2017-08-02")
        #return int(x / np.timedelta64(1, 'W'))
        return (x).apply(lambda x: x/np.timedelta64(1,'W')).astype(int)

    #https://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python
    #Create a generator to iterate through a range of dates
    def daterange(self, startDate, endDate):
        for n in range(int((endDate - startDate).days)):
            yield startDate + timedelta(n)
        
    def setDFForCounting(self, dataframe):
        self.dfCopy = dataframe.copy()
        self.dfCopy['DateOnly'] = self.dfCopy['Time'].dt.date   #object
        self.dfCopy['TimeRepeat'] = self.dfCopy['Time']
        self.dfCopy = self.dfCopy.set_index('Time')
        #self.dfCopy.info()
        #print(self.dfCopy)
        #print(self.dfNight)

        for singleDate in self.daterange(pd.to_datetime(self.startDate), pd.to_datetime(self.endDate)):

            #Create a dfNight = df0_7pm-12am + df1_12am-7am
            self.dfDay0 = self.dfCopy[self.dfCopy.DateOnly == pd.to_datetime(singleDate)]
            self.dfDay1 = self.dfCopy[self.dfCopy.DateOnly == pd.to_datetime(singleDate+timedelta(days=1))]
            
            df_7pm_12am = self.dfDay0.between_time('19:00', '23:59')
            df_12am_7am = self.dfDay1.between_time('00:00', '07:00')
            self.dfNight = pd.concat([df_7pm_12am, df_12am_7am])
            print(self.dfNight)

            #Number of feeds at night
            try:
                numOfNursing = self.dfNight['Resource'].value_counts().Nursing
            except:
                numOfNursing = 0

            try:
                numOfBottlePump = self.dfNight['Resource'].value_counts().BottlePumped
            except:
                numOfBottlePump = 0

            try:
                numOfBottleFormula = self.dfNight['Resource'].value_counts().BottleFormula
            except:
                numOfBottleFormula = 0

            numOfFeeds = numOfNursing + numOfBottlePump + numOfBottleFormula
            #numOfFeeds = dfNight['Resource'].value_counts().Nursing + dfNight['Resource'].value_counts().BottlePumped + dfNight['Resource'].value_counts().BottleFormula           
            #Number of sleeps at night
            numOfSleeps = self.dfNight['Resource'].value_counts().Sleep
            print(singleDate.strftime("%Y-%m-%d") + " Night: #ofFeeds=" + str(numOfFeeds) + ", #ofWakes=" + str(numOfSleeps-1))
            #print(singleDate.strftime("%Y-%m-%d") + ": " + str(numOfSleeps))

            #Reset the index from Time to integer increment
            self.dfNight = self.dfNight.reset_index(drop=True)
            #print(self.dfNight)
            #Get indices of feedings
            listOfFeedings = self.dfNight.index[(self.dfNight['Resource'] == "Nursing") | (self.dfNight['Resource'] == "BottlePumped") | (self.dfNight['Resource'] == "BottleFormula")].tolist()
            print(listOfFeedings)
            self.calculateTimeFromLastFeeding(listOfFeedings, self.dfNight)


    def setDataFrameDateRange(self, startDate, endDate):
        #print(self.df)
        mask = (self.df.Time > startDate) & (self.df.Time < endDate)
        self.df = self.df.loc[mask]
        self.df = self.df.sort_index().reset_index(drop=True)
        #print(self.df)

    def addRowAfterMidnightSleep(self):
        #Find indexes of dates after this time - 
        #when Ben fell asleep after 6:40pm and woke up after midnight
        compareStartDate = pd.to_datetime(["2017-08-02 18:40:00"])
        compareEndDate = pd.to_datetime(["2017-08-03 00:10:00"])
        #https://stackoverflow.com/questions/18327624/find-elements-index-in-pandas-series
        #https://stackoverflow.com/questions/17241004/how-do-i-get-a-dataframe-index-series-column-as-an-array-or-list
        midnight_indices = (self.df[((self.df["Time_SameDate2"] > compareStartDate[0]) 
                            & (self.df["EndTime_SameDate2"]>compareEndDate[0]))].index.values) 
        #print("midnight indices")                                                                
        #print(midnight_indices)

        #Insert a new row after these indices. Make EndTime of new row the same as EndTime of indexA
        for indexA in midnight_indices:
            #https://stackoverflow.com/questions/15888648/is-it-possible-to-insert-a-row-at-an-arbitrary-position-in-a-dataframe-using-pan?rq=1
            line = pd.DataFrame({'Time_SameDate2': pd.to_datetime(["2017-08-02 00:00:00"]),
                                 'EndTime_SameDate2': self.df.EndTime_SameDate2[indexA] - pd.Timedelta(days=1), 
                                 'DateString': self.df.DateString[indexA+1], 
                                 'Resource': 'Sleep'}, index=[indexA+0.5])
            self.df = self.df.append(line, ignore_index=False)

        #Move EndTime_SameDate2 to midnight. 
        for indexA in midnight_indices:
            self.df.iloc[indexA, self.df.columns.get_loc('EndTime_SameDate2')] = pd.to_datetime(["2017-08-03 00:00:00"])

        self.df = self.df.sort_index().reset_index(drop=True)

    def addDummyRowAtEnd(self):
        #Add a dummy row at the end. Needed for addRowAfterMidnightSleep()
        dummyLastDateTimeEntry = pd.to_datetime(str(self.endDate) + ' 23:58:00') - timedelta(days=1)
        dfLastDateTime = pd.DataFrame({
            "Time":[dummyLastDateTimeEntry], 
            "TotalDuration":[1],
            "Resource":["Sleep"]
            })
        self.df = self.df.append(dfLastDateTime, ignore_index=True)
        #print(self.df)

    def addFirstSleepEntry(self):
        #Find first nursing Time / index 0. Add in row at top. 
        #Time = startTime, TotalDuration = firstNursingTime - midnight
        firstTimeValue = self.df.iloc[0]['Time'] #Access first row as a series with iloc. dateTime value
        #print(firstTimeValue)
        dummyFirstDateTimeEntry = pd.to_datetime(str(self.startDate) + ' 00:00:00')
        #print(dummyFirstDateTimeEntry)
        dummyTotalDuration = firstTimeValue - dummyFirstDateTimeEntry
        dummyTotalDuration_min = dummyTotalDuration.seconds/60
        
        dfFirstDateTime = pd.DataFrame({
            "Time":[dummyFirstDateTimeEntry], 
            "TotalDuration":[dummyTotalDuration_min],
            "Resource":["Sleep"]
            })
        self.df = self.df.append(dfFirstDateTime, ignore_index=True)
        
        #Sort dataframe by Time column. Reset the index
        self.df = self.df.sort_values(by='Time').reset_index(drop=True)
        #print(self.df)


if __name__ == "__main__":
    testClass = Data(filename='1to6month.csv', 
                    startDate="2017-09-02",
                    endDate="2017-09-06")
    #print(testClass.df)

    #Export to CSV
    testClass.df.to_csv (r'export_dataframe.csv', index=True, header=True)
    