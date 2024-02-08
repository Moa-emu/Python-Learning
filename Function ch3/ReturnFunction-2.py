
#RETURN STATEMENTS AND RETERN VALUES
#- return values are a way to output values within a function all you have to do is type a return statement in your function
#ex below:
import random

def giveRandomNumber(numRange):
    pickedNumber = random.randint(1,numRange)
    return pickedNumber

userNum = int(input(('type a number and I will give you a random number from (1 - your number):')))
randomNumber = giveRandomNumber(userNum)
print(f'Here is your random number: {randomNumber}')








#THE NONE VALUE
#- in python none represents a data type with the absence of a value
#- you must type none like this: None
#- it is useful with Functions in Python that do not explicitly return a value return None by default. This is useful for indicating that a function did not produce a result or that it has completed its task without returning a value
#- None can act as a placeholder for a variable that has not yet been given a value. It's a way to signify that a variable exists but has no particular value

#here is an example below
# Define a function that returns None
def return_none():
    return None
# Call a function that returns None and print its result
none_result = return_none()
print("Function with None return value returns:", none_result)



