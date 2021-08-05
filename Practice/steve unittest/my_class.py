from dataclasses import dataclass
'''
Dataclass are just a convienent way of creating a class which 
automatically creates an __init__ function for you that assigns 
all the values listed as inputs and sets them in self. 
For example, this is the Input class using dataclasses and 
OtherWayToDoInputs is (mostly) equivalent but without using dataclass. 
I say "mostly" because likely there are other added features that 
dataclass gives you that I'm not aware of.
'''

@dataclass
class Inputs:
  value1: float
  value2: float

class OtherWayToDoInputs:
  def __init__(self, value1, value2):
    self.value1 = value1
    self.value2 = value2

@dataclass
class Outputs:
  output1: float

'''
Simple class for processing Inputs into Outputs.
Class is initilized with an optional scalar value which defaults to 1. 
ProcessStuff() returns the sum of the two input values (which are 
contained in the single Input object) multiplied by the scalar.
'''
class DoStuffClass:
  def __init__(self, scalar=1):
    self.scalar = scalar

  def ProcessStuff(self, inputs):
    output = self.__PrivateFunction(inputs)
    outputs = Outputs(output1=output)
    return outputs
  
  # This is a private function. It cannot be called from outside the class.
  def __PrivateFunction(self, inputs):
    return self.scalar * (inputs.value1 + inputs.value2)
