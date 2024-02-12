# Slicing strings in Python allows you to extract a portion of a string by specifying a range of indices. Here's a brief explanation using examples:

#The syntax for slicing a string is string[start:stop:step], where:

# start: The index of the first character to include in the slice. If omitted, the slice starts at the beginning of the string.
# stop: The index of the first character to exclude from the slice. If omitted, the slice goes to the end of the string.
# step: The number of characters to skip between each character in the slice. If omitted, the default step is 1, which means no characters are skipped.


# Define a string
string = "Hello, World!"

#Extract charcter from index 1
slice0 = string[0]
print(slice0) #output: "h"

# Extract characters from index 1 up to (but not including) index 3
slice1 = string[1:3]
print(slice1)  # Output: "el"

# Extract characters starting from index 1 until the end of the string
slice2 = string[1:]
print(slice2)  # Output: "ello, World!"


stringvar = "Hello, World!"

# Get the first character
first_char = stringvar[0]  # Output: 'H'

# Get the first three characters
first_three_chars = stringvar[:3]  # Output: 'Hel'

# Get characters  4,  5, and  6
slice_four_five_six = stringvar[4:7]  # Output: 'o,'