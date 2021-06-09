import sys

def calculateAverage1(*args):
    print(args)
    argCount = len(args)
    if argCount > 0:
        #start summing
        sum = 0 #initialize
        for element in args[1:]:
            sum += element

        return sum / argCount
    else:
        return 0

def calculateAverage2(listOfArguments):
    print(listOfArguments)
    listOfArguments = listOfArguments[1:] #Remove first one = name of test script
    #Use list comprehension to convert str to int
    listOfArguments = [int(i) for i in listOfArguments]
    listOfArguments.sort()
    print(listOfArguments)
    print(len(listOfArguments))
    argCount = len(listOfArguments)
    if argCount > 0:
        sum = 0
        for i in listOfArguments:
            sum = sum + i
        return sum / argCount
    else:
        return 0

if __name__ == "__main__":
   
    #print(calculateAverage1(1,2,3))

    arguments = sys.argv
    print("Number of arguments: ", len(sys.argv))
    print("Argument list: ", str(sys.argv))

    print(calculateAverage2(arguments))

    #Usage: python variableArguments.py 1 3 10