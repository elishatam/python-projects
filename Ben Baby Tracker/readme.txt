For Ben Baby Tracker
To run, need python 3.8

Open up command prompt, navigate to git\python-projects\Ben Baby Tracker
type: workon py38generic
python guiGraph.py


This is the while loop that updates:
1) TKinter GUI = guiGraph.py
2) Graph if in widgetMenu.py, needToUpdateGraphFlag = 1 because change date

prepareData.py, line 169 has print(obj_days[i].__dict__)
widgetDays.py, line 49 has print(lst)

To do
- in widgetDays.py, change Entry to Label so it's not editable? https://www.tutorialspoint.com/python/tk_entry.htm
- X  Clear widgetDays when update
-    Add scroll bar to Days widget?
-    How come some dates have 2 entries?