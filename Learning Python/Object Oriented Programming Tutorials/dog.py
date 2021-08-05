'''
#https://realpython.com/python3-object-oriented-programming/
#Class = blueprint for an object = form
#Instantiate an object from a class = many different filled out forms.
#Attributes and methods define the properties and behaviors of an object
#Use inheritance to create child classes from a parent class
#arguments (application side) are assigned to parameters (definition side) 

3 pillars of OOP
- Encapsulation - hide internal data/variables. Only expose what's needed for the user
- Inheritance
- Polymorphism
'''
class Dog:
    #class attribute
    species = "Canis familiaris"  #This is the same value for all class instances

    #init method. The properties that all Dog objects must have are defined in init
    #Sets the initial state of the object
    def __init__(self, name, age):
        #instance attributes - these vary from one instance to another
        self.name = name  #name attribute
        self.age = age

    #dunder method = double underscores at beginning and end
    #Special instance method
    def __str__(self):
        return f'{self.name} is {self.age} years old'

    #Instance method
    def description(self):
        return f'{self.name} is {self.age} years old'

    #Another instance method. It has a parameter
    def speak(self, sound):
        return f'{self.name} says: {sound}'

    def getDog():
        print("This is a static class method. No self as a parameter")
        #In main, do Dog.getDog(). Can't have an instance call this.

    #This is a static class method. No self as a parameter
    def print_all_dogs(dogs):
        for dog in dogs:
            print(dog)

#Create new child classes that inherit from Dog class
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        #return f'{self.name} says {sound}'
        return super().speak(sound)  #use parent's output but modify the sound
                                    #Python searches the parent class for a .speak() method
                                    #and calls it with the variable sound

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)


if __name__ == "__main__":
    buddy = Dachshund("Buddy", 9)
    miles = JackRussellTerrier("Miles", 4)
    jack = Bulldog("Jack", 3)
    patti = Bulldog("patti", 5)

    print(buddy.age)  #Access their instance attributes with dot notation
    print(buddy.species) #Access class attributes
    print(miles.speak())
    print(miles)  #This uses the special instance method
    print(miles.speak("bow"))
    print(patti.speak("woof"))

    dogsList = [Bulldog("Jim", 5), JackRussellTerrier("Miles", 4), Dachshund("Buddy", 9)]

    Dog.print_all_dogs(dogsList)