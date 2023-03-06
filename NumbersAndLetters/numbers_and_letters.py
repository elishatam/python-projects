
from time import sleep
import sys
#https://stackoverflow.com/questions/17432478/python-print-to-one-line-with-time-delay-between-prints

def printThis(lastNumber=10, delay_s=0.1):
    for i in range(1, lastNumber+1):
        print(i, end='')
        sys.stdout.flush()  #Output is buffered when print without new line.
                            #Need to flush stdout
        sleep(delay_s)
    


if __name__ == "__main__":
    
    try:
        lastNumber=int(sys.argv[1])
        delay_s=float(sys.argv[2])
    except IndexError:
        lastNumber=10
        delay_s=0.1    
    
    printThis(lastNumber=lastNumber, delay_s=delay_s)

