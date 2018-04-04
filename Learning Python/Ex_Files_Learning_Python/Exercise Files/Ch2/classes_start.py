#
# Example file for working with classes
#

class myClass():
    #self = refers to object itself
    #First argument of a method of a class is self
    def method1(self):
        print("myClass method1")
        
    def method2(self, someString):
        print("myClass method2 " + someString)

#Inherit from myClass
class anotherClass(myClass):
    #self = refers to object itself
    #First argument of a method of a class is self
    def method1(self):
        myClass.method1(self)  #call the inherited method on the super class
        print("anotherClass method1")
        
    def method2(self, someString):
        print("anotherClass method2 ")
def main():
    #instantiate class
    c = myClass()
    c.method1()
    c.method2("This is a string")
  
    c2=anotherClass()
    c2.method1()    #call the inherited method on the super class
    c2.method2("This is a string")
    
if __name__ == "__main__":
  main()
