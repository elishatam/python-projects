'''
This script moves the mouse every few seconds/minutes between 2 mouse locations
'''
import pyautogui
import time

if __name__ == "__main__":
    delayBetweenMouseMoves_sec = 10 
    startTime = int(round(time.time()))
    moveToLocation = 0
    print("moveToLocation: " + str(moveToLocation)+". delay: " + str(delayBetweenMouseMoves_sec))
    while True: 
        if moveToLocation == 0:
            if (int(round(time.time())) - startTime) >= delayBetweenMouseMoves_sec:
                pyautogui.moveTo(100, 500, duration = 1)
                startTime = int(round(time.time())) #new start time  
                moveToLocation = 1
                print("moveToLocation: ", moveToLocation)
        else:
            if (int(round(time.time())) - startTime) >= delayBetweenMouseMoves_sec:     
                pyautogui.moveTo(1000, 500, duration = 1)
                startTime = int(round(time.time())) #new start time  
                moveToLocation = 0
                print("moveToLocation: ", moveToLocation)


    