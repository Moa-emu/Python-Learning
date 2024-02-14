

#LIST LIKE OBJECTS
# - as you are already aware there or things that you can do with list that you do with other objects like strings such as indexing,slicing, using loops with them, len(), in and not in and other things
#MUTABLE AND IMMUTABLE DATA TYPES
#   - even  though lsit and strings have alot of things in common there is
#     one important thing the don't a LIST is a MUTABLE DATA TYPE while
#     STRINGS are IMMUTABLE

#- MUTABLE: means the ability to change you can change/replace
#           charcters in a list but you can not do that to a string such as:
# name = Billy
# name[3] = 'M' #- this would give you an error if done to string
# you can only mutate a string with concatonation and slicing

#Below is how List are Mutable:
whatIWant = ['happyness', 'Freedom', 'Money', 'Family'] 
# I am going to mutate  this list
whatIWant = ['Money', 'House', 'Pets', 'Good Food']
# NOTE the main lesson here is that I did not overwite the code
#  I just made a copy of whatIwant if you actually want  to modify  the original list you got to do something like I do below
BestStandsJOJO = ['KingKrimson', 'StarPlatinum', 'Golden Wind', 'Echo act IIII']
del BestStandsJOJO[0:4]#deleted all of the items
print(BestStandsJOJO)
BestStandsJOJO.append('Za Worldo')
BestStandsJOJO.append( 'Soft and Wet')
BestStandsJOJO.append( 'Tusk actIII')
BestStandsJOJO.append( 'Crazy Dimond')
print(BestStandsJOJO)