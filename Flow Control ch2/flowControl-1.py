#-flow control allows programers to decide to skip instructions and repeat them depending upon how expressions are evaluated

#explain flow chart since it is a good visual representation of this concept

#Boolean Values are data types that are evaluated as true or false
#   - remember that they are always evaluted as capital True and False
happy = True
print('I am happy !')
print('are you happy ' + str(happy)) # this will print true
sad = False
print('are you sad ' +  str(sad))



#Comparison Operators
#   - these are used to compare two values and evaluate them to True or False
# Here are the comparison operators

# == : equal to
#remember that = is for assining and == is for equal to 
#ex: below
7 == 7 #this will return true
7 == 6 #this will return false
'star wars' == 'star trek' # this returns false (can even use for strings)
42 == 42.0 #this returns true
#Remember that an interger or float will never be equal ot a string value
42 == '42' # this will return false

# != : not equal to 
#ex: below
7 != 3 # this will return true since 7 is not equal to 3
7 != 7 # this will return false since they are in fact equal to each other
'star wars' != 'star treck' # this returns false


# <  : less than
#ex: below
5 < 10 # this will return true
10 < 5 # this will return false
 

# >  : greater than
#ex: below
a = 5
b = 9
print("is 9 greater than 5 " + str(b > a)) #returns true

# <= : less than or equal to 
a = 3
b = 9
print("is 9 less than or equal to 5 " + str(b <= a)) # returns fals

# >= : greater than or equal to 
a = 3
b = 9
print("is 9 greater than or equal to 5 " + str(b >= a)) #returns true 







 #Logical Operators

#REMEMBER THAT PYTON DOES NOT USE THE SYMBOLS
# AND(&&) - this takes two boolean values 
#   - the condition is that both boolean values must be true to evaluate as true any other case and it is false
#ex: below
a = 5
b = 9
c = 10
#also for the logical operators you can use the symbol or type out the word in python
print ((b > a) and (b < 10)) # this will evaluate to true



# OR(||) - this takes two boolean values
#   - atleast one has to be true for it to evaluate to true 
#ex: below
print (True or False) #this will evaluate to true even though
print ((False) or (False)) #this will evaluate to false no condition is true


# NOT(!) - this takes one boolean value and just changes it to its oposite
#ex: below
print (not True) # this will evaluate to false
print (not False)# this will evaluate to true

#last but not least when mixing logical operators remember that  the computer will read from the left then to right
#also remember that there is an order of operation not operators are evaluated first, then and operators and lastly or operators