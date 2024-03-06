#   As you are well aware with python we are able to handle text data in many ways 
#such as concatonating strings but in this chapter we will focus on how you cna do
#more like removing spaces, converting letters to lower case or uppercase, and even
#copying and pasting text in your computers clipboard.


#WORKING WITH STRINGS


#Double qoutes(" ")
#------------------------
#   - in python you can use double qoutes the same way you use single qoutes
#   - it also helps so that if you put a single qoute for an apostraphe 
#   -example: 
mySpeech = "Hello I belive in America's mission"






#Escape Characters(\)
#-----------------------
#   -These are ways for you to use characters into strings 
#   - Below are escape characters you can use:
#   (\') single qoute
#   (\") double qoute
#   (\t) tab 
#   (\n) newline\ linebreak
#   (\\) Backslash
#   -example:
print("Hello there!\nHow are you?\nI\'m doing fine.")
#it prints:
# Hello there!
# How are you?
# I'm doing fine.







#Raw strings
#------------
#these are like f strings, but what they do is just ignore all of the escape charcter key
#example: 
print(r'Hello I am Venessa\'s cat.')
#it prints: Hello I am Venessa\'s cat.






#MULTILINE STRINGS  with Triple Quotes
#   - this is a way t ouse strings that span mulpiple lines
#Here is an example: 
text =''' This is a
multiline 
string'''
print(text)
#it prints: 
#  This is a
# multiline
# string

#YOU CAN EVEN USE MULTILINE STRINGS FOR COMMENTS

''' 
Hello there I am trying to communicate with you

I belive that we should try to be nicer people
'''

# Here are some more things that we have done before but just reminding
#   -INDEXING AND SLICING STRINGS
        #using things like string[-1] for the lat character
        #string[0:5] the first character to fifth character
        #string[6:] sixth character and above
        #string[:5] fifth charcter and below
#   -IN AND NOT IN OPERATOR WITH STRINGS
        # stuff like 'Hello' in 'hello World' will return True

#   -upper(),lower(),isupper(), and islower() METHOD
        #makes strings or certain characters uppercase,lowercase or checking for both



#Here is the isX String Methods
#   -isalpha() this checks if a string contains an alphabet character
print('Hello'.isalpha()) # this prints True


#   -isalnum() this checks if a string contains only letters and numbers and is not blank
print('123345'.isalnum()) #prints True

#   -isdecimal() this checks if a string has a nemeric charcters and is not blank
print('123'.isdecimal()) #prints True

#   -isspace() this checks if a string contains a space
print(' '.isspace()) #prints True

#   -istitle() this contains if a string is in title case
print('This Is The Best'.istitle()) #print True









#The join() and split() STRING METHOD
# -join: useful when you have a list of strings that you want to put together in a single string
# -split: this is useful to divide a string into a list of substrings based on a specific category if no category is specified it will jsut slit at whitespace characters
print(','.join(['cats', 'dragon', 'bats']))
#prints: cats,dragon,bats

print(' '.join(['Hello', 'how', 'are', 'you']))
#prints: Hello how are you

text2 = "Hello, there you silly person"
print(text2.split()) #it will print: ['Hello,', 'there', 'you', 'silly', 'person']

#Here is using the split with a category
text3 = "cats,dogs,dragons"
print(text3.split(',')) # it will print: ['cats', 'dogs', 'dragons']




#JUSTIFYING TEXT WITH rjust(),ljust(), and center()
#These are functions that will add space to either move the text left, rig
# the first argument represents how many spaces it will be moved 
# the second argument represents what character you want to replace the space with

print('Hello'.rjust(10,'-'))
#This prints: -----Hello
print('My Name'.ljust(20,'*'))
#This prints: My Name*************














 