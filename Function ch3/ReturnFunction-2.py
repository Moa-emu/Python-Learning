
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