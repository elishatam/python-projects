import plotly.plotly as py
import plotly.figure_factory as ff

df = [
    dict(Task='Baby', Start='2017-08-15 23:00:00', Finish='2017-08-16 00:43:00', Resource='Sleep'),
    dict(Task='Baby', Start='2017-08-16 0:43:00', Finish='2017-08-16 0:48:00', Resource='DiaperWet'),
    dict(Task='Baby', Start='2017-08-16 0:50:00', Finish='2017-08-16 1:21:00', Resource='Nurse'),
    dict(Task='Baby', Start='2017-08-16 1:24:00', Finish='2017-08-16 3:39:00', Resource='Sleep'),
    dict(Task='Baby', Start='2017-08-16 3:41:00', Finish='2017-08-16 4:29:00', Resource='Nurse'),
    dict(Task='Baby', Start='2017-08-16 4:39:00', Finish='2017-08-16 5:29:00', Resource='Sleep'),
    dict(Task='Baby', Start='2017-08-16 5:30:00', Finish='2017-08-16 5:35:00', Resource='DiaperWet'), 
    dict(Task='Baby', Start='2017-08-16 5:34:00', Finish='2017-08-16 6:31:00', Resource='Nurse'),
    dict(Task='Baby', Start='2017-08-16 6:35:00', Finish='2017-08-16 08:50:00', Resource='Sleep'),
    dict(Task='Baby', Start='2017-08-16 8:55:00', Finish='2017-08-16 09:40:00', Resource='Nurse'),
    dict(Task='Baby', Start='2017-08-16 9:24:00', Finish='2017-08-16 09:29:00', Resource='DiaperWet'),
    dict(Task='Baby', Start='2017-08-16 10:31:00', Finish='2017-08-16 10:36:00', Resource='DiaperWet'),
    dict(Task='Baby', Start='2017-08-16 10:38:00', Finish='2017-08-16 11:13:00', Resource='Nurse'),
    dict(Task='Baby', Start='2017-08-16 11:20:00', Finish='2017-08-16 12:44:00', Resource='Sleep'),
    dict(Task='Baby', Start='2017-08-16 12:46:00', Finish='2017-08-16 13:34:00', Resource='Nurse'),
    dict(Task='Baby', Start='2017-08-16 13:45:00', Finish='2017-08-16 13:50:00', Resource='DiaperWet'),
    dict(Task='Baby', Start='2017-08-16 14:50:00', Finish='2017-08-16 15:52:00', Resource='Nurse'),
    dict(Task='Baby', Start='2017-08-16 16:30:00', Finish='2017-08-16 16:35:00', Resource='DiaperBM'),
    dict(Task='Baby', Start='2017-08-16 17:00:00', Finish='2017-08-16 17:15:00', Resource='Nurse'),  #bottle
    dict(Task='Baby', Start='2017-08-16 17:15:00', Finish='2017-08-16 17:51:00', Resource='Sleep'),
    dict(Task='Baby', Start='2017-08-16 19:04:00', Finish='2017-08-16 19:09:00', Resource='DiaperWet'),
    dict(Task='Baby', Start='2017-08-16 19:12:00', Finish='2017-08-16 19:27:00', Resource='Nurse'),
    dict(Task='Baby', Start='2017-08-16 19:37:00', Finish='2017-08-16 21:00:00', Resource='Sleep'),
    dict(Task='Baby', Start='2017-08-16 21:04:00', Finish='2017-08-16 21:56:00', Resource='Nurse'),
    dict(Task='Baby', Start='2017-08-16 22:30:00', Finish='2017-08-16 22:35:00', Resource='DiaperWet'),
    dict(Task='Baby', Start='2017-08-16 22:55:00', Finish='2017-08-16 23:20:00', Resource='Nurse'),

    dict(Task='Mom', Start='2017-08-15 23:00:00', Finish='2017-08-16 00:40:00', Resource='Sleep'),
    dict(Task='Mom', Start='2017-08-16 0:50:00', Finish='2017-08-16 1:21:00', Resource='Nurse'),
    dict(Task='Mom', Start='2017-08-16 1:30:00', Finish='2017-08-16 3:34:00', Resource='Sleep'),
    dict(Task='Mom', Start='2017-08-16 3:41:00', Finish='2017-08-16 4:29:00', Resource='Nurse'),
    dict(Task='Mom', Start='2017-08-16 4:44:00', Finish='2017-08-16 5:24:00', Resource='Sleep'), 
    dict(Task='Mom', Start='2017-08-16 5:34:00', Finish='2017-08-16 6:31:00', Resource='Nurse'),
    dict(Task='Mom', Start='2017-08-16 6:40:00', Finish='2017-08-16 08:45:00', Resource='Sleep'),
    dict(Task='Mom', Start='2017-08-16 8:55:00', Finish='2017-08-16 09:40:00', Resource='Nurse'),
    dict(Task='Mom', Start='2017-08-16 10:38:00', Finish='2017-08-16 11:13:00', Resource='Nurse'),
    dict(Task='Mom', Start='2017-08-16 12:46:00', Finish='2017-08-16 13:34:00', Resource='Nurse'),
    dict(Task='Mom', Start='2017-08-16 14:50:00', Finish='2017-08-16 15:52:00', Resource='Nurse'),
    dict(Task='Mom', Start='2017-08-16 19:12:00', Finish='2017-08-16 19:27:00', Resource='Nurse'),
    dict(Task='Mom', Start='2017-08-16 21:04:00', Finish='2017-08-16 21:56:00', Resource='Nurse'),
    dict(Task='Mom', Start='2017-08-16 22:55:00', Finish='2017-08-16 23:20:00', Resource='Nurse'),

    dict(Task='Nonparent', Start='2017-08-15 23:00:00', Finish='2017-08-16 07:00:00', Resource='Sleep'),
    dict(Task='Nonparent', Start='2017-08-16 08:00:00', Finish='2017-08-16 08:30:00', Resource='Eat'),
    dict(Task='Nonparent', Start='2017-08-16 09:00:00', Finish='2017-08-16 12:00:00', Resource='Work'),
    dict(Task='Nonparent', Start='2017-08-16 12:00:00', Finish='2017-08-16 13:00:00', Resource='Eat'),
    dict(Task='Nonparent', Start='2017-08-16 13:00:00', Finish='2017-08-16 18:30:00', Resource='Work'),
    dict(Task='Nonparent', Start='2017-08-16 19:30:00', Finish='2017-08-16 20:00:00', Resource='Eat'), 
    dict(Task='Nonparent', Start='2017-08-16 20:00:00', Finish='2017-08-16 23:00:00', Resource='Rest')
]

colors = dict(Sleep = 'rgb(46, 137, 205)', #blue
              Rest = 'rgb(244, 235, 66)',  #yellow
              Nurse = 'rgb(198, 47, 105)',
              DiaperBM = 'rgb(211, 141, 10)',   #brown
              Eat = 'rgb(244, 66, 66)',   #red
              Work = 'rgb(58, 0, 136)',   #purple
              DiaperWet = 'rgb(164, 244, 66)', #green             
              Bottle = 'rgb(242, 104, 242)') #pink

fig = ff.create_gantt(df, colors=colors, index_col='Resource', title='Daily Schedule',
                      show_colorbar=True, bar_width=0.2, showgrid_x=True, showgrid_y=True, group_tasks=True)
py.iplot(fig, filename='2weeks', world_readable=True)