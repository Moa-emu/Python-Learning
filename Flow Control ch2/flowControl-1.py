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
print("is 9 greater than 5 " + str(b > a))

# <= : less than or equal to 
a = 3
b = 9
print("is 9 greater than 5 " + str(b <= a))

# >= : greater than or equal to 
a = 3
b = 9
print("is 9 greater than 5 " + str(b >= a)) #returns true



 