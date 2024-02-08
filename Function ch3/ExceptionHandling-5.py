#Exception Handling
#Normally when you get an error in your program your program crashes
#but real world programers use try and except statements so that their programs can detect if they encounter an error to stop from crashing


#below is an example since we know that dividing by 0 gives an ZeroDivisionError so this program uses try and except statements to catch it instead of crashing the program

def divideNum(numToDivide):
    #try basically is just us telling the program to do this
    try:
        return 100 / numToDivide
    #except just is if a certain error occurs exevure the code in the clause and coninue as normal
    except ZeroDivisionError:
        print('Error: Invalid argument')

print(divideNum(9))
print(divideNum(200))
print(f'{divideNum(0)} \n')





#below shows that any errors in the try block will also be caught even if not in a function
def divideNumTry(Divide):
    return 100 / Divide

#try basically is just us telling the program to do this
try:
    print(divideNumTry(9))
    print(divideNumTry(200))
    print(divideNumTry(0))
#except just is if a certain error occurs exevure the code in the clause and coninue as normal
except ZeroDivisionError:
    print('Error: Invalid argument')