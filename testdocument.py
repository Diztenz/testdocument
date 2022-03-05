# Test document for Dad

#from curses import keyname
import time



def function0():
    print("Zero")
    #press the zero key

def function1():
    print("One")
    #press the one keyname
def function2():
    print("Two")
def function3():
    print("Three")

def function4():
    print("Four")

def function5():
    print("Five")

def function6():
    print("Six")

def function7():
    print("Seven")

def function8():
    print("Eight")

def function9():
    print("Nine")

for x in range(9999+1):
    y = str(x)
    numDigits = len(y)
    if numDigits == 1:
        a = '0'
        b = '0'
        c = '0'
        d = y
    elif numDigits == 2:
        a = '0'
        b = '0'
        c = y[0]
        d = y[1]
    elif numDigits == 3:
        a = '0'
        b = y[0]
        c = y[1]
        d = y[2]
    else:
        a = y[0]
        b = y[1]
        c = y[2]
        d = y[3]
        
    print(a+b+c+d)
    e = (a + b + c + d)
    for j in range(4):
        servoNumber = e[j]
        if servoNumber == '0':
            function0()
        elif servoNumber == '1':
            function1()
        elif servoNumber == '2':
            function2()
        elif servoNumber == '3':
            function3()
        elif servoNumber == '4':
            function4()
        elif servoNumber == '5':
            function5()
        elif servoNumber == '6':
            function6()
        elif servoNumber == '7':
            function7()
        elif servoNumber == '8':
            function8()
        elif servoNumber == '9':
            function9()


#etc.
print("Goodbye")