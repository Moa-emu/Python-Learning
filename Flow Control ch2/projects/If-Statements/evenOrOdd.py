# this is from exercise 34 from python workbook


# Write a program that reads an integer from the user. Then your program should
#display a message indicating whether the integer is even or odd.



print('type a number and we will tell you if it is even or odd')
#below gets the users input as an interger
userNum = int(input())

#if the userNum modulo 2 has no remainder then it is even
if (userNum % 2 == 0 ):
    print('the number ' + str(userNum) + ' is even')

#else it has to be odd
else:
    print('your number is odd')