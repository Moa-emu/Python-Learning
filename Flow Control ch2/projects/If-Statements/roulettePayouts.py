# this is exercise 60


# A roulette wheel has 38 spaces on it. Of these spaces, 18 are black, 18 are red, and two
# are green. The green spaces are numbered 0 and 00. The red spaces are numbered 1,
# 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30 32, 34 and 36. The remaining integers
# between 1 and 36 are used to number the black spaces.
# Many different bets can be placed in roulette. We will only consider the following
# subset of them in this exercise:
# • Single number (1 to 36, 0, or 00)
# • Red versus Black
# • Odd versus Even (Note that 0 and 00 do not pay out for even)
# • 1 to 18 versus 19 to 36
# Write a program that simulates a spin of a roulette wheel by using Python’s random
# number generator. Display the number that was selected and all of the bets that must
# be payed. For example, if 13 is selected then your program should display:
# The spin resulted in 13...
# Pay 13
# Pay Black
# Pay Odd
# Pay 1 to 18
# If the simulation results in 0 or 00 then your program should display Pay 0 or
# Pay 00 without any further output.


#below I am importing random so I can use it
#Also I am setting 37 to 00
import random
rouletteSpin = random.randint(0,37)


#below will be the logic for the spin
if  (rouletteSpin == 1 or rouletteSpin == 3 or rouletteSpin == 5 or rouletteSpin == 7 or 
    rouletteSpin == 9 or rouletteSpin == 12 or rouletteSpin == 14 or rouletteSpin == 16 or 
    rouletteSpin == 18 or rouletteSpin == 19 or rouletteSpin == 21 or rouletteSpin == 23 or 
    rouletteSpin == 25 or rouletteSpin == 27 or rouletteSpin == 30 or rouletteSpin == 32 or 
    rouletteSpin == 34 or rouletteSpin == 36):
    spinColor = 'black'

elif rouletteSpin == 37:
    rouletteSpin = '00'
    spinColor = 'green'
    divisibility = 'odd'
    payRange = '00'

elif rouletteSpin == 0:
    spinColor = 'green' 
    divisibility = 'odd' 
    payRange = '0'

else:
    spinColor = 'red'


if (rouletteSpin % 2 == 0) and (rouletteSpin != 0) and (rouletteSpin != 37):
    divisibility = 'even'
else:
    divisibility = 'odd'


if (rouletteSpin <= 18):
    payRange = 'pay 1 to 18'
else:
    payRange = 'pay 19 to 36'


#below ask the player if they want to play

print('do you want to play (y or n):')
playerResponse = input()
if playerResponse == 'y':
    print(f'The spin resulted in {rouletteSpin}...')
    print(f'pay {rouletteSpin}')
    print(f'pay {spinColor}')
    print(f'pay {divisibility}')
    print(payRange)
else:
    print('have a nice day')