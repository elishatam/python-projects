
class Car:

	def __init__(self, make, color, mileage):
		self.make = make
		self.color = color
		self.mileage = mileage


	def __str__(self):
		return f'The {self.make} is {self.color} and has {self.mileage:,} miles'


	def whatColor(self):
		#print("hello")
		print(f'This car is {self.color}')
		return


if __name__ == "__main__":
	snoopy = Car("Toyota", "White", 20000)
	george = Car("BMW", "grey", 30000) 

	print(snoopy)
	snoopy.whatColor()
	print(snoopy.color)