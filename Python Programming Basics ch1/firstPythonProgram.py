# You will create a program that will ask the user for their name and save it then it will print a greeting  with the user's name tell the user the length of their name and finally aks the user for their age and then tell the user what their age will be in a year

# Here are some functions that you should know before you start the program

# input() function
#   - this function waits for the user to type text with their keyboard and then press enter
#   - You can use the input function to then assain the users input into a variable ex: name = input()

# len()function 
#   -this function can be used to count the amount of characters within a string
#   -ex: print(len('Hello there earthlings.')) - The output will be 23 meaning 23 characters

# str(), int(), and float() functions
#   -These will change datatypes into other datatatypes for example: str(29) - this will turn the interger of 29 into a string data type


# Here is my implementation of the program:
print('Hello how are you what is your name: ')
userName = input()
#Below you can see that I am using string concatonation
print('Hello ' + userName + ', I hope you are having a good day!')
characterCount = len(userName)
# We are changing the character count into a string so that we can concatonate it
print('Also your name has ' + str(characterCount)  + ' characters in it.')
print('Last but not least what is your age: ')
userAge = input()
futureAge = int(userAge) + 1
print('Interesting you are ' + str(userAge) + ', that means you will be ' + str(futureAge) + ' in one year.')

 