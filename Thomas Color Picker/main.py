#import cs2000Wrapper as cs2000
import time
#from leia_color_library import *
#import leia_color_library

colors = ['white', 'green', 'blue', 'red']
ip = 'http://192.168.1.117:8081'
#camera = cs2000.CS2000(mode='color', log=False)

for c in colors:
    #set_display_color(ip, c)
    time.sleep(1)
    #x, y, L = camera.measure()
    #print(c, x, y, L)
    print(c)


# D = [[542.6,	0.2983,	0.3265],
#      [102.4,	0.6577,	0.3096],
#      [341.9,	0.2518,	0.6864],
#      [41.61,	0.1511,	0.0641]]
#
# xt = 0.2937
# yt = 0.2747
#

# correct_white_point(D, xt, yt)
# plt.show()
