"""https://www.youtube.com/watch?v=tmY6FEF8f1o"""

import matplotlib.pyplot as plt

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	#operator overloading. Without this, Python didn't know how to add 2 Points
	#https://www.geeksforgeeks.org/operator-overloading-in-python/
	def __add__(self, other):
		#If "other" is an instance of a Point, then add the points.
		if isinstance(other, Point):
			x = self.x + other.x
			y = self.y + other.y
			return Point(x,y)
		else:
			x = self.x + other
			y = self.y + other
			return Point(x,y)

	def plot(self):
		plt.scatter(self.x, self.y)

a = Point(1,1)
b = Point(2,2)

#a.plot()
#plt.show()

#c = a+b
#print(c.x, c.y)
d = a + 5
print(d.x, d.y)