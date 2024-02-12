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




