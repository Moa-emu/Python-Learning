#EXPLAINING THE LIST DATA TYPE

# The List data type and it's relative the Tuple are capable of containing
# multiple values helping programers handle large amounst of data
#Also since list can hold other list then can be able to arage data into hierarchical structures.

#List syntax => listName = [ value1, value2, value3 ,....]
#List can contain any data type inside of them they do not have to be the same data type
#The values inside are called items
#below is an example
campingSupplies = ['Backpack', 'Tent', 'HickingBoots', 'Knife']
RandomList = ['hello', ['I love you', 'you are my sunshine'], 9, 100, 100.52]


#______________________________________________________________________________________________________
#INDEXING ITEMS IN A LIST

# - like all things that involve counting in programming list items start at 0 and then increase
# - you can index a list just like you index a string
#example below:
print(campingSupplies[0]) #this will output Backpack
print(campingSupplies[:2]) #this will output the first 2 values in camping supplies
print(RandomList[1][1])# this will output you are my sunshine # isn't that cool a list in a list multilist of maddness
print(RandomList[4]) # this will output 100.52
#below you can see me concatonate a list item with a string
print(f'Hello, {RandomList[1][1]}')# this will print Hello, you are my sunshine

#DO NOT INDEX A NUMBER THAT EXCEEDS YOU LIST VALUES - IT WILL GIVE YOU AN ERROR
#ALSO DO NOT DO ANYTHING STUPID LIKE => ListName[1.0] - That will give you an error


#___________________________________________________________________________________________________________________________________

#NEGATIVE INDEXES
#   - Just like with strings if you try to do a negative index it will go from last to first
# Ex: below:
campingSupplies = ['Backpack', 'Tent', 'HickingBoots', 'Knife']
#Negative values start from -1 since you can not have -0 That just doesn't make sense
print(campingSupplies[-2]) # this will print our HickingBoots

#__________________________________________________________________________________________________________________________________

#SLICING A LIST -List slicing in Python allows you to access a subset of the elements within a list. You can specify the start and end indices, and optionally the step value to determine the frequency at which elements are included in the resulting sublist.

#Examples below
# Original list
numbers = [0,  1,  2,  3,  4,  5,  6,  7,  8,  9]

# Slice the first three items
first_three = numbers[:3]  # Output: [0,  1,  2]

# Slice the last three items
last_three = numbers[7:]  # Output: [7,  8,  9]

# Reverse the entire list
reversed_list = numbers[::-1]  # Output: [9,  8,  7,  6,  5,  4,  3,  2,  1,  0]

# Take every other item, starting from the first
every_other = numbers[::2]  # Output: [0,  2,  4,  6,  8]

# Take every third item, starting from the second
third_items = numbers[1::3]  # Output: [1,  4,  7]

#________________________________________________________________________________________________________________________________________________________________________________________

#USING LEN() ON A LIST
spam = ['cat', 'dog', 'moose']
print(len(spam)) # this will give you 3 since there are 3 items in the list

#______________________________________________________________________________________________________________________________________________________________________________________________________




#CHANGING A LIST'S VALUE WITH INDEXES
#   -look below to see how you can do that 
campingSupplies = ['Backpack', 'Tent', 'HickingBoots', 'Knife']

campingSupplies[1] = 'Hammock' # now instead of Tent there will be Hammock
campingSupplies[2] = campingSupplies[3] # now are list is ['Backpack', 'Hammock', 'Knife', 'Knife']
campingSupplies[-1] =  'snowboard' # now are list is ['Backpack', 'Hammock', 'Knife', 'snowboard']


#___________________________________________________________________________________________________________________________________________________________________________________________________________________



#LIST CONCATENATION AND LIST REPLICATION
# - the (+) operator can combine two list and the (*) operator with an interger value can be use to duplicate a list
#Ex below:
alphabet = ['A','B','C']
numbers = ['1', '2', '3']

combinedList = alphabet + numbers
print(combinedList) # this will print ['A', 'B', 'C', '1', '2', '3']

#below we will even multiply a list
numbersThree = numbers * 3
print(numbersThree) #thiw will print ['1', '2', '3', '1', '2', '3', '1', '2', '3']
 
#_____________________________________________________________________________________________________________________________________________

#REMOVING LIST Items WITH THE DEL Statement

#simply just write: del listName[index]
#ex: below

animals = ['Lion', 'Elephant', 'Fox', 'bat']
del animals[2]
print(animals)# now the list is ['Lion', 'Elephant', 'bat']

#____________________________________________________________________________________________________________________________________________________________


#WORKING WITH LIST IN YOUR PROGRAMS

# below I will show you how to make a program taht will allow the user to keep adding names to the list
freinds = []
while True:
    #below we are also using str(len(freinds))to find out what freind the user is on
    print('type stop when you want to stop')
    ask = str(input(f'What are the names of your friend #{str(len(freinds) + 1)}: '))
    #below will add the name of the freind to the list
    
    if ask == 'stop':
        break

    freinds += [ask] # we do it like [variable] to show that we want to add it in list format
        
print(f'Here are all of your freinds names: ')
#below will be a for loop to print out all of your freinds names
for name in freinds:
    print(name)






#Below is way for you to acsess a list's index with a loop
FreirenCharacters = ['Friren', 'Himmel the Hero', 'Heiter', 'Eiesen', 'Fern', 'Stark', 'Sein']
#below will be a for loop that will print out all of the characters and their index
for i in range(len(FreirenCharacters)):
    print(f'In Index #{i} there is the charcter: {FreirenCharacters[i]}')




#__________________________________________________________________________________________________________________________________________________




