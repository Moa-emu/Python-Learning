#below will be a short program to show all the stuff that we learned

import random
def guessNumber():
    randomNumber = random.randint(1,20)
    #the for loop will track how many guess have happend when guesses get to 7 and you have not guessed the right number game over
    for guessTaken in range(1,7):
            #below is the guesses the player can make
        guess = int(input('Take a guess: '))
        if guess != randomNumber:
            if guess > randomNumber:
                print('your guess is too high, try again')
            elif guess < randomNumber:
                print('Your guess is too low, try again')
        else:
            print('great job! you have guessed the number')
            break
    #in python you can use else clauses with for loops to do a block of code when the loop is finished
    #the else below is for when the for loop finishes and the user has not guessed the number
    else:
        print('you have no more guesses,sorry')

print('I am thinking of a number between 1 and 20. you have 6 guesses.')
guessNumber()