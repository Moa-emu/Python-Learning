#F-Strings -used for printing formatted strings allows you to embed expressions inside string literals, which are then evaluated at runtime and formatted into the final string.
#ex: below
name = "John"
age = 30

# Basic usage with variables
print(f"My name is {name} and I am {age} years old.")

# Using expressions
half_age = age / 2
print(f"Half my age is {half_age}")

# Formatting with precision
pi = 3.14159
print(f"Pi rounded to two decimal places is {pi:.2f}")

# Date formatting
from datetime import datetime
current_time = datetime.now()
print(f"Current time is {current_time:%H:%M:%S}")