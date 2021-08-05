'''
#https://www.youtube.com/watch?v=MikphENIrOo
3 pillars of OOP
- Encapsulation - hide internal data/variables. Only expose what's needed for the user
- Inheritance
- Polymorphism - multiple classes inherit from 1 class.
'''
class User:
	def log(self):
		print(self)

class Teacher(User):
	#Derived class has an override of log()
	def log(self):
		print("I'm a teacher!")


class Customer(User):
	def __init__(self, name, membership_type):
		self.name = name
		self.membership_type = membership_type

	#These properties are getting invoked anytime we set or get the value of name
	@property #Decorator to show extra functionality. 
	def name(self):
		#print("getting name")
		return self._name  #Private. Don't touch this unless within class

	@name.setter
	def name(self, name):
		#print("setting name")
		self._name = name

	#@name.deleter
	#def name(self):
	#	del self._name

	def update_membership(self, new_membership):
		print("Calculating costs")
		self. membership_type = new_membership

	def __str__(self):
		return self. name + " " + self.membership_type

	def print_all_customers(customers):
		for customer in customers:
			print(customer)

	def __eq__(self, other):
		if self.name == other.name and self.membership_type == other.membership_type:
			return True

		return False

	__hash__ = None

	__repr__ = __str__

users = [Customer("Caleb", "Gold"),
			Customer("John", "Silver"),
			Teacher()]

#print(customers)
#customers[2].log()

for user in users:
	user.log()