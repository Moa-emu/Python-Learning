#This is exercise 72

# A string is a palindrome if it is identical forward and backward. For example “anna”,
# “civic”, “level” and “hannah” are all examples of palindromic words. Write a program
# that reads a string from the user and uses a loop to determines whether or not it is a
# palindrome. Display the result, including a meaningful output message.


#Below we will ask the user for a string
print('please enter a word and I will tell you if it is a palindrome or not:')
userinput = str(input())
#below will be where are reversed string will be contained
backwardString = ''


#remember that if string = hello  , then string[-1] = o it goes backwards
#also remember that len(string) will return the length of a string

 #below we will use a for loop to make the string go backwards
#remember that range(start, end, step) end must be one less than desired value
for i in range(len(userinput)-1, -1, -1):
    #below will add the letter to the backwards sting for every iteration
    backwardString += userinput[i]
 
if backwardString == userinput:
    print('your word is a palindrome')
else:
    print('your word is not a palindrome')