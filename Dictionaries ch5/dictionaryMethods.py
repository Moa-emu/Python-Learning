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
    print(f"The state Animal of {stateAnimals[key]} is the {stateAnimals[value]}")