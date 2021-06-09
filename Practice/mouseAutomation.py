'''
This script pressesm the "right" button every "delayBetweenMouseMoves_sec"
'''
import pyautogui
import time
from random import randrange

def moveMouse(xloc, yloc, duration):
    pyautogui.moveTo(xloc, yloc, duration = duration)

def keyPress():
    pyautogui.press('right')

if __name__ == "__main__":
    #delayBetweenMouseMoves_sec = 10
    randomSecValueMax = 30 
    delayBetweenMouseMoves_sec = randrange(randomSecValueMax) 
    startTime = int(round(time.time()))
    print("Max Delay: " + str(randomSecValueMax))
    while True:
        if (int(round(time.time())) - startTime) >= delayBetweenMouseMoves_sec:
            keyPress()
            delayBetweenMouseMoves_sec = randrange(30)   #Choose new delay
            #print("Delay: " + str(delayBetweenMouseMoves_sec))
            startTime = int(round(time.time())) #new start time  
            


#This is to move mouse from location0 to location1
'''
    while True: 
        if moveToLocation == 0:
            if (int(round(time.time())) - startTime) >= delayBetweenMouseMoves_sec:
                #moveMouse(xloc=100, yloc=500, duration = 1)
                keyPress()
                startTime = int(round(time.time())) #new start time  
                moveToLocation = 1
                #print("moveToLocation: ", moveToLocation)
        else:
            if (int(round(time.time())) - startTime) >= delayBetweenMouseMoves_sec:     
                #moveMouse(xloc=1000, yloc=500, duration = 1)
                keyPress()
                startTime = int(round(time.time())) #new start time  
                moveToLocation = 0
                #print("moveToLocation: ", moveToLocation)
'''

    