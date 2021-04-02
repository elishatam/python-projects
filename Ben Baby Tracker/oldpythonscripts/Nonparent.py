import plotly.plotly as py
import plotly.figure_factory as ff

df = [
    dict(Task='Nonparent', Start='2016-01-01 23:00:00', Finish='2016-01-02 07:00:00', Resource='Sleep'),
    dict(Task='Nonparent', Start='2016-01-02 08:00:00', Finish='2016-01-02 08:30:00', Resource='Eat'),
    dict(Task='Nonparent', Start='2016-01-02 09:00:00', Finish='2016-01-02 12:00:00', Resource='Work'),
    dict(Task='Nonparent', Start='2016-01-02 12:00:00', Finish='2016-01-02 13:00:00', Resource='Eat'),
    dict(Task='Nonparent', Start='2016-01-02 13:00:00', Finish='2016-01-02 18:30:00', Resource='Work'),
    dict(Task='Nonparent', Start='2016-01-02 19:30:00', Finish='2016-01-02 20:00:00', Resource='Eat'), 
    dict(Task='Nonparent', Start='2016-01-02 20:00:00', Finish='2016-01-02 23:00:00', Resource='Rest')
]

colors = dict(Sleep = 'rgb(46, 137, 205)', #blue
              Rest = 'rgb(244, 235, 66)',  #yellow
              Nurse = 'rgb(198, 47, 105)',
              BM = 'rgb(211, 141, 10)',   #brown
              Eat = 'rgb(244, 66, 66)',   #red
              Work = 'rgb(58, 0, 136)',   #purple
              Wet = 'rgb(164, 244, 66)', #green             
              Bottle = 'rgb(242, 104, 242)') #pink

fig = ff.create_gantt(df, colors=colors, index_col='Resource', title='Daily Schedule',
                      show_colorbar=True, bar_width=0.2, showgrid_x=True, showgrid_y=True, group_tasks=True)
py.iplot(fig, filename='Nonparent', world_readable=True)
