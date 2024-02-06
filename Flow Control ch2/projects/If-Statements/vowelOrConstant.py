#this is exercise 36


# In this exercise you will create a program that reads a letter of the alphabet from the
# user. If the user enters a, e, i, o or u then your program should display a message
# indicating that the entered letter is a vowel. If the user enters y then your program
# should display a message indicating that sometimes y is a vowel, and sometimes y is
# a consonant. Otherwise your program should display a message indicating that the
# letter is a consonant.



# (IN) operator is useful for seeing if something is within some strings 

print('Enter a character and we will tell you if it is a vowel or constant')

#below will get the users input
userChar = input()

if (userChar in 'aeiouAEIOU' ):
    print('That letter is a vowel')

elif(userChar in 'yY'):
    print('Sometimes the letter y is a vowel, and sometimes it is a constant')

else:
    print('That letter is a constant.')


