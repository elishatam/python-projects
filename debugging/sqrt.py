import math
import random

def square_root(x, eps = 10e-7):
    assert x >= 0
    y = math.sqrt(x)
    #assert y * y == x
    #set up a suitable post condition
    assert abs(((y*y) - x)) < eps
    return y

for i in range(1, 10):
    r = random.random() * 10000
    try:
        z = square_root(r)
        print(r, math.sqrt(r) * math.sqrt(r), (r - (math.sqrt(r) * math.sqrt(r))))
    except:
        print(r, math.sqrt(r) * math.sqrt(r), (r - (math.sqrt(r) * math.sqrt(r))))
        break


#print("Done")