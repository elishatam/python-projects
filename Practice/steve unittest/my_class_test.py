import my_class

# Test with scalar of 1 which is the default
my_object = my_class.DoStuffClass()

input = my_class.Inputs(value1=2, value2=3)
output = my_object.ProcessStuff(input)
assert output.output1 == 5

input = my_class.Inputs(value1=1, value2=1)
output = my_object.ProcessStuff(input)
assert output.output1 == 2

# Test with scalar of -2
my_object = my_class.DoStuffClass(-2)

input = my_class.Inputs(value1=2, value2=3)
output = my_object.ProcessStuff(input)
assert output.output1 == -10 

# You can access "self" data from the object with a simple . operator.
# This works for all classes, not just dataclasses. See below:
print(f'scalar for object \'my_object\' = {my_object.scalar}')

# The following line if commented out will fail because we cannot call
# a private function of a class directly from an object of that class.
# my_object.__PrivateFunction(input)

print('Success!')
