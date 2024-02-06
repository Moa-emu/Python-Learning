# This is exercise 59

# In a particular jurisdiction, older license plates consist of three uppercase letters
# followed by three numbers. When all of the license plates following that pattern had
# been used, the format was changed to four numbers followed by three uppercase
# letters.
# Write a program that begins by reading a string of characters from the user. Then
# your program should display a message indicating whether the characters are valid
# for an older style license plate or a newer style license plate. Your program should
# display an appropriate message if the string entered by the user is not valid for either
# style of license plate.

print("enter a liscence plate:")
userInput = input()

#Below is how you can slice a string
#remember that stringvar[0] gets the first character
#stringvar[:3] gets the first 3 characters
#stringvar[4:7] gets the characters 4,5,6
#below is an example
#print('here is the first  characters:' + str(userInput[:3]))

#you can use the .isalpha() - to find out if something is a letter
#you can use the .isupper() - to find out if something is a upper case letter
#you can use the .isdigit() - to find out if something is a number

#below will check if it is a old liscence plate
if (userInput[:3].isupper) and (userInput[4:6].isdigit):
    print('you have a old lisence plate')

elif (userInput[:4].isdigit) and (userInput[5:7].isupper):  
    print('you have a new lisence plate')

else:
    print('your lisence plate is not valid try again')