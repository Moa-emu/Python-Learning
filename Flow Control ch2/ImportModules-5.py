#IMPORTING MODULES
#   - all python programs come with built in features and functions if you want to bring another modules functions, variables, and classes to use in your current project you will have to use the import module 
#- to use it all you have to do is type the import keyword along with the name of the module
#- if you want to add more module names you will have to separate them with commas
#ex: - i will use the random module
import random
#- you might have to search up what you will have to do to invoke those modules
#-random.randint(a,b)- a & b are just the parameters
scare = random.randint(1, 10 )
print('I will scare you at a random time')
for i in range(1, 11, 1):
    if i == scare:
        print("boo")
    else:
        print(i)
print("did I scare you")

# there are other modules such as the math module, sys.exit() module and many more