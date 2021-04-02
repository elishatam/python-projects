'''
Name: Day class
Summary: Sets up specific parameters for Day object
         
'''
class Day:
    def __init__(self, date, dfNight, numOfNightFeeds, numOfNightWakes):
        self.date = date
        self.dfNight = dfNight
        self.numOfNightFeeds = numOfNightFeeds
        self.numOfNightWakes = numOfNightWakes
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
