#The Tuple Data Type 
#-The tuples is simlar to list but they have a few differences: below
# - Tuples use () instead of []
# - Tuples are Imutable,their values can not be modified,appended or removed

#Tuple examples below
words = ('hello', 'Exubarated', 'Hacking', 'Cipher', 'Wolf')
print(words[0]) #prints: hello
print(words[1:4]) #prints: ('Exubarated', 'Hacking', 'Cipher')


#YOU CAN DO EVERYTHING THAT YOU CAN DO WITH A LIST BUT YOU CAN NOT APPEND, REMOVE OR MODIFY


#You can even convert Types with list() and tuple() functions


# Using the tuple() function:
sample_list = ['apple', 'banana', 'cherry']
# Convert list to tuple
tuple1 = tuple(sample_list)
print(tuple1)  # Output: ('apple', 'banana', 'cherry')



# Using unpacking with the * operator:
my_list = ['Spark', 'Python', 'Pandas', 'Java']
# Convert list to tuple using * operator
tuples = (*my_list,)
print(tuples)  # Output: ('Spark', 'Python', 'Pandas', 'Java')




# Converting a Tuple to a List:
# Using the list() function:
sample_tuple = ('apple', 'banana', 'cherry')
# Convert tuple to list
list1 = list(sample_tuple)
print(list1)  # Output: ['apple', 'banana', 'cherry']




# Using unpacking with the * operator:
my_tuple = ('Spark', 'Python', 'Pandas', 'Java')
# Convert tuple to list using * operator
my_list = [*my_tuple]
print(my_list)  # Output: ['Spark', 'Python', 'Pandas', 'Java']