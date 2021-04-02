from itertools import cycle
import pandas as pd
import numpy as np
'''
Name: Day class
Summary: Sets up specific parameters for Day object
         
'''
class Day:
    def __init__(self, date, dfNight, numOfNightFeeds, numOfNightWakes, longestTimeBtwnFeeds, longestTimeBtwnFeeds_T0):
        self.date = date
        self.dfNight = dfNight
        self.numOfNightFeeds = numOfNightFeeds
        self.numOfNightWakes = numOfNightWakes
        self.longestTimeBtwnFeeds = longestTimeBtwnFeeds
        self.longestTimeBtwnFeeds_T0 = longestTimeBtwnFeeds_T0
    '''
    def __init__(self, date, dfNight, longestTimeBtwnFeeds, longestTimeBtwnFeeds_T0, numOfNightFeeds, numOfNightWakes): 
        self.date = date
        self.dfNight = dfNight  #Defined as date_7pm to date+1_7am
        self.longestTimeBtwnFeeds = longestTimeBtwnFeeds
        self.longestTimeBtwnFeeds_T0 = longestTimeBtwnFeeds_T0
        self.numOfNightFeeds = numOfNightFeeds
        self.numOfNightWakes = numOfNightWakes
    '''    

    def countNumOfNightFeeds(self):
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

        return numOfFeeds

    def countNumOfNightWakes(self):
        numOfSleeps = self.dfNight['Resource'].value_counts().Sleep
        return numOfSleeps - 1


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
        #print(df_feeds)
        longestTimeBetweenFeeds = df_feeds["Time Difference"].max()
        index_longestTimeBetweenFeeds = df_feeds["Time Difference"].idxmax()
        time0_longestTime = df_feeds["Time0"][index_longestTimeBetweenFeeds]
        time1_longestTime = df_feeds["Time1"][index_longestTimeBetweenFeeds]
        #print("longest time since last feeding (min): " + str(longestTimeBetweenFeeds) + " at index: " + str(index_longestTimeBetweenFeeds) + 
        #    ". " + str(time0_longestTime) + " and " + str(time1_longestTime))

        self.longestTimeBtwnFeeds = longestTimeBetweenFeeds
        self.longestTimeBtwnFeeds_T0 = time0_longestTime