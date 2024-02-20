#DICTIONARY METHODS - KEYS(), VALUES(), ITEMS()

# There are three really important dictionary methods when it comes to
# returning a dictionaries keys, values or both.
# these methods are keys(), values(), and items()

#Since Dictionaries are immutable objects they cannot be modified in ways like
#appendind. Although yuou can still use the (dict_keys, dict_values and 
#dict_items) in for loops 
#example below:  

stateAnimals = {'Texas': 'Longhorn', 'New Mexico': 'Black Bear', 'Arizona':'Ringtail', 'Utah': 'Elk', 'Colorodo': 'Big horn sheep', 'California': 'Grizzly Bear', 'Oklahoma': 'Bison', 'Florida': 'Manatee or Dolphin'}

#Printing values
for value in stateAnimals.values():
    print(value)
# it prints: 
# Longhorn
# Black Bear
# Ringtail
# Elk
# Big horn sheep
# Grizzly Bear
# Bison
# Manatee or Dolphin
#----------------------------------------------   
#printing keys
for key in stateAnimals.keys():
    print(key)
#it prints:
# Texas
# New Mexico
# Arizona
# Utah
# Colorodo
# California
# Oklahoma
# Florida
#-----------------------------------------------------
#printing items
for key,value in stateAnimals.items():
    print(f"The state Animal of {key} is the {value}")
#it prints: 
# The state Animal of Texas is the Longhorn
# The state Animal of New Mexico is the Black Bear
# The state Animal of Arizona is the Ringtail
# The state Animal of Utah is the Elk
# The state Animal of Colorodo is the Big horn sheep
# The state Animal of California is the Grizzly Bear
# The state Animal of Oklahoma is the Bison
# The state Animal of Florida is the Manatee or Dolphin
#-----------------------------------------------------------------------------
#This will print all of the items in a tuple like format
for i in stateAnimals.items():
    print(i)
#it prints: 
# ('Texas', 'Longhorn')
# ('New Mexico', 'Black Bear')
# ('Arizona', 'Ringtail')
# ('Utah', 'Elk')
# ('Colorodo', 'Big horn sheep')
# ('California', 'Grizzly Bear')
# ('Oklahoma', 'Bison')
# ('Florida', 'Manatee or Dolphin')
#--------------------------------------------------------------------------------------------
#Below will be how you can check if a key or  value exists in a dictionary
    #Below will check if Texas is a key
print('Texas' in stateAnimals.keys())
#it will print:True

    #Below will check if Elk is a value 
print('Elk' in stateAnimals.values())
#it will print:True

    #Below will check if Lion is not in values
print('Lion' not in stateAnimals.values())
# it will print:True
#--------------------------------------------------------------------------------------------------------------------------

#The GET() METHOD
# - This is a less tedious way to check wheather a key exist in a dictionary
# before you acsessing the keys value. The get method takes two parameters, 
# the key of the value that you want to revtreve and a fallback value to return
# if the key does not exist.
shoppingList = {'Bread':3, 'Eggs': 5, 'Juice':3}
print(f"When I go to the store I will get {str(shoppingList.get('Bread', 0))} Bread Cases.")
print(f"When I go to the store I will get {str(shoppingList.get('Chocolate', 0))} Peices of Chocolate")

#-----------------------------------------------------------------------------------------------------------------------------------

#THE SETDEFAULT() METHOD
# The setdefault method in Python is a dictionary method that returns the 
# value of a key if the key is in the dictionary. If the key is not found, 
# it inserts the key with a specified default value into the dictionary. 
# The syntax for setdefault is as follows:
# dict.setdefault(key, default_value)

# Here's an example of using setdefault when the key is already in the 
# dictionary:
d = {'a':  97, 'b':  98}
print("setdefault() returned:", d.setdefault('b',  99))
print("After using setdefault():", d)
#This is what will be printed out: 
    # setdefault() returned:  98
    # After using setdefault(): {'a':  97, 'b':  98}


# here's an example of using setdefault when the key is not in the dictionary:
Dictionary1 = {'A': 'Geeks', 'B': 'For'}
ret_value = Dictionary1.setdefault('C', "Geeks")
print("Return value of setdefault():", ret_value)
print("Dictionary after using setdefault():", Dictionary1)
#this is what it will print out: 
    # Return value of setdefault(): "Geeks"
    # Dictionary after using setdefault(): {'A': 'Geeks', 'B': 'For', 'C': "Geeks"}


# One important thing to note is that the setdefault method will always evaluate the second argument, even if the key exists in the dictionary. This means that if the second argument is an expression that has side effects (like a function call), it will be executed every time setdefault is called, which can be inefficient



#Below is a way to use the set Default method to count the number of occurrences of each letter in a string
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
 count.setdefault(character, 0)
 count[character] = count[character] + 1
print(count)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#PRETTY PRINTING
#pretty printing and pretty format is a module in python that allows you to 
#to make your printing of a dictionary look better. Helpful when you want to
#display a dictionary in a better format.
#to use them just import pprint
#Below is an example:
import pprint 
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
 count.setdefault(character, 0)
 count[character] = count[character] + 1
#to use it just type pprint.pprint
pprint.pprint(count)

#It will print:
# {' ': 13,
#  ',': 1,
#  '.': 1,
#  'A': 1,
#  'I': 1,
#  'a': 4,
#  'b': 1,
#  'c': 3,
#  'd': 3,
#  'e': 5,
#  'g': 2,
#  'h': 3,
#  'i': 6,
#  'k': 2,
#  'l': 3,
#  'n': 4,
#  'o': 2,
#  'p': 1,
#  'r': 5,
#  's': 3,
#  't': 6,
#  'w': 2,
#  'y': 1}

# If you want to obtain the prettified text as a string value instead of 
#displaying it on the screen, call pprint.pformat() instead. These two lines
#are equivalent to each other:
# pprint.pprint(someDictionaryValue)
# print(pprint.pformat(someDictionaryValue))
