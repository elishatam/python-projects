"""https://www.youtube.com/watch?v=tmY6FEF8f1o
"""
import turtle

class Polygon:

	def __init__(self, sides, name, size=100, color="black", line_thickness=3):
		self.sides = sides
		self.name = name
		self.size = size
		self.color = color
		self.line_thickness = line_thickness
		self.interior_angles = (self.sides-2)*180
		self.angle = self.interior_angles/self.sides

	#class method
	def draw(self):
		turtle.color(self.color)
		turtle.pensize(self.line_thickness)
		for i in range(self.sides):
			turtle.forward(self.size)
			turtle.right(180-self.angle)
		

#Inheritance. Utilize Polygon as the parent class and Square is the subclass
class Square(Polygon):
	def __init__(self, size=100, color="black", line_thickness=3):
		super().__init__(4, "Square", size, color, line_thickness) #take from super class.

	#method overwriting
	def draw(self):
		turtle.begin_fill()
		super().draw()
		turtle.end_fill()


if __name__ == '__main__':
	square = Square()
	pentagon = Polygon(5, "Pentagon")
	hexagon = Polygon(6, "Hexagon", color="red")

	print(square.name, square.sides, square.interior_angles, square.angle)

	print(pentagon.name, pentagon.sides, pentagon.interior_angles, pentagon.angle)

	square.draw()
	hexagon.draw()

	turtle.done()