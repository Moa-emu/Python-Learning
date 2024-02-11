# In Python, you can use the math module to perform various mathematical operations such as rounding numbers up (math.ceil), down (math.floor), or to the nearest whole number (round). Here's an example demonstrating each of these functions:
# In this example:

# math.ceil() is used to round up the number to the next highest integer 134.
# math.floor() is used to round down the number to the next lowest integer 134.
# round() is used to round the number to the nearest integer. When given a second argument, it specifies the number of decimal places to round to


import math

# Using math.ceil to round up
num_to_ceil =  10.123
result_ceil = math.ceil(num_to_ceil)
print("math.ceil(10.123):", result_ceil)  # Output:  11




# Using math.floor to round down
num_to_floor =  10.987
result_floor = math.floor(num_to_floor)
print("math.floor(10.987):", result_floor)  # Output:  10





# Using round to round to the nearest whole number
num_to_round =  10.5
result_round = round(num_to_round)
print("round(10.5):", result_round)  # Output:  11




# Using round with precision
num_to_precision =  10.333
result_precision = round(num_to_precision,  2)
print("round(10.333,  2):", result_precision)  # Output:  10.33


