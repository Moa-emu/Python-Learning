#REFRENCES & PASSING REFRENCES 
#   -The premise of this topic is that when you assign a list to a variable
#    you are not act ually assigning a list to the variable. You are assinging
#    a list refrence to the variable.

# WHAT IS A REFRENCE: This is a value that points to some bit of data, a list
#                     refrence is a value that points to a list

#Below is an example to make it easier to understand

mountains = ['Everest', 'Kilamingaro', 'Fuji', 'Rocky Mountains', 'Andes']

#below I will assign mountains t oanother variable
mountainRanges = mountains

#now I will change mountain ranges
mountainRanges[0] = 'St.Helen'

# you will see now that both mountainRanges and mountains are both affected
print(mountainRanges) #prints: ['St.Helen', 'Kilamingaro', 'Fuji', 'Rocky Mountains', 'Andes']
print(mountains) #prints: ['St.Helen', 'Kilamingaro', 'Fuji', 'Rocky Mountains', 'Andes']

#THE MAIN TAKE AWAY IS THAT IN PYTHON CHANGING A REFRENCE ALSO CHANGES THE ORIGINAl
# you can do this to List and Dictionaries 