import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

t = np.arange(0.0, 100.0, 0.1)
s = np.sin(2*np.pi*t)
l, = plt.plot(t,s)
plt.axis([0, 10, -1, 1])

axcolor = 'lightgoldenrodyellow'
#plt.axes([left, bottom, width, height])
axpos = plt.axes([0.2, 0.1, 0.65, 0.03], axisbg=axcolor)

#Slider(ax, label, valmin, valmax)
spos = Slider(axpos, 'Pos', 0.1, 90.0)

def update(val):
    pos = spos.val
    #axis(xmin, xmax, ymin, ymax)
    ax.axis([pos,pos+10,-1,1])
    fig.canvas.draw_idle()

spos.on_changed(update)

plt.show()