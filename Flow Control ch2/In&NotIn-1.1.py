# In Python, the in and not in operators are used to check for membership. These operators determine whether a given value is a constituent element of a sequence, such as a string, array, list, or tuple, returning True or False.

# in Operator: Returns True if the specified value is found within the sequence.
# not in Operator: Returns True if the specified value is not found within the sequence.



# Example using 'in' operator
sentence = "Hello, how are you?"
print('how' in sentence)  # Output: True

# Example using 'not in' operator
print('world' not in sentence)  # Output: True

# In the first example, 'how' in sentence returns True because the substring 'how' is indeed part of the string sentence. In the second example, 'world' not in sentence returns True because the substring 'world' is not present in sentence


#more explanation if needed:
# An in operator can connect two strings, and it will evaluate to True if the first string is inside the
# second string or evaluate to False if not. The in operator can also be paired with not, which will do the
# opposite. Enter the following into the interactive shell:

'hello' in 'hello world!'
# returns True

'hello' not in 'hello world!'
# returns False

'ello' in 'hello world!'
# returns True

'HELLO' in 'hello world!'
# retruns False

'' in 'Hello'
# retruns True


# Notice that the in and not in operators are case sensitive . Also, a blank string is always
# considered to be in any other string .
# Expressions using the in and not in operators are handy to use as conditions of if statements to
# execute some code if a string exists inside another string.








#Below is some stuff outside of the scope of chapter 2
# Using 'in' operator
numbers = [1,  2,  3,  4,  5]
print(3 in numbers)  # Output: True
print('dog' in 'the dog jumped over the fence')  # Output: True

# Using 'not in' operator
print('cat' not in 'the dog jumped over the fence')  # Output: True
print(99 not in range(1,  100))  # Output: True


# It's important to note that the in and not in operators can be used with various data types, including:

# Lists, tuples, and ranges
# Strings
# Generators
# Dictionaries and sets