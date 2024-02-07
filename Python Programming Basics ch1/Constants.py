# Constants are variables whose values are meant to stay the same once they are assigned. They represent fixed values that are universally true and do not change over time.
# In Python, constants are not enforced by the language itself. They are treated like regular variables, but by convention, developers use uppercase letters for their names to indicate that they should be treated as constants.
# To DECLARE a constant, you simply assign a value to a variable with an all-uppercase name, like CONSTANT = 50.
# Although the naming convention indicates that a constant should not be changed, Python does not prevent you from reassigning a value to the variable. It is up to the programmer to respect this convention and not modify the value.
# Constants are often defined in a separate module and then imported into other modules where they are needed. This keeps the constants organized and accessible throughout the project.


# ere is an example of how you might define and use constants in Python:

# In a module named constants.py
PI =  3.14159
GRAVITY =  9.81

# In another module where you want to use these constants
# import constants

# print('Value of PI:', constants.PI)
# print('Value of Gravity:', constants.GRAVITY)