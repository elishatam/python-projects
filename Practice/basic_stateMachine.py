import signal
import sys #parse command line arguments

myState = "STATE1"

'''
Name: Switcher(object)
Summary: Switch statement class to implement Motor Initialization State Machine
'''
class Switcher(object):

    '''
    Name: switchState(self, argument)
    Summary: Call this continually in a while loop to run through the switch statement
    Args: string for the state. (Example: "CHOOSEMOTOR")
    Return: method that runs the state (Example: CHOOSEMOTOR() method is run)
    '''
    def switchState(self, argument):
        '''Dispatch method'''
        methodName = argument
        #Get the method from 'self'. Default to a lambda.
        method = getattr(self, methodName, lambda: "Invalid entry")
        #Call the method as we return it
        return method()

    def STATE1(self):
        global myState
        print("In STATE1")
        input("Press Enter to continue...")

        
        myState = "STATE2"
        return

    def STATE2(self):
        global myState
        print("In STATE2")
        input("Press Enter to continue...")

        myState = "STATE3"
        return

    def STATE3(self):
        global myState
        print("In STATE3")
        input("Press Enter to continue...")

        myState = "STATE4"
        return

    def STATE4(self):
        global myState
        print("In STATE4")
        input("Press Enter to continue...")

        myState = "DONE"
        return



    '''
    Name: DONE(self)
    Summary: Done
    '''
    def DONE(self):
        print("In DONE")
        input("Press Enter to continue...")
        sys.exit(1)
        return



def runProgram():
    a = Switcher() #This is an instance of the statemachine switch statement

    while True:
        a.switchState(myState)    

#Reference:https://stackoverflow.com/questions/18114560/python-catch-ctrl-c-command-prompt-really-want-to-quit-y-n-resume-executi
def exit_gracefully(signum, frame):
    # restore the original signal handler as otherwise evil things will happen
    # in input when CTRL+C is pressed, and our signal handler is not re-entrant
    signal.signal(signal.SIGINT, original_sigint)

    try:
        if input("\nReally quit? (y/n)> ").lower().startswith('y'):
            sys.exit(1)

    except KeyboardInterrupt:
        print("Ok ok, quitting")
        sys.exit(1)

    # restore the exit gracefully handler here    
    signal.signal(signal.SIGINT, exit_gracefully)        


if __name__ == "__main__":
    # store the original SIGINT handler
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)
    runProgram()