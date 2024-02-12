# String slicing in Python allows you to extract a subset of a string, effectively getting a new string that contains a part of the original string. 
#The syntax for slicing a string is string[start:stop:step], where:

# start: The index of the first character to include in the slice. If omitted, the slice starts at the beginning of the string.
# stop: The index of the first character to exclude from the slice. If omitted, the slice goes to the end of the string.
# step: The number of characters to skip between each character in the slice. If omitted, the default step is 1, which means no characters are skipped.

# Example string
stringvar = "Hello, World!"

# Get the first character
first_char = stringvar[0]  # Output: 'H'

# Get the first three characters
first_three_chars = stringvar[:3]  # Output: 'Hel'

# Get characters  4,  5, and  6
slice_four_five_six = stringvar[4:7]  # Output: 'o,'