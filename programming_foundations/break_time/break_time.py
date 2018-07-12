import time
import webbrowser

total_breaks = 3
break_count = 0

print("This program started on "+time.ctime())

while(break_count < total_breaks):
    time.sleep(10) #in seconds
    webbrowser.open("http://www.google.com")
    break_count = break_count + 1


"""
wait_time = 10
last_breaktime = time.ctime()

while(break_count < total_breaks):
    if ((int(time.ctime()) - last_breaktime) < wait_time) :
        webbrowser.open("http://www.google.com")
        last_breaktime = time.ctime()
        break_count = break_count + 1
"""