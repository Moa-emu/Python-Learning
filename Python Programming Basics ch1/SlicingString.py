# Slicing strings in Python allows you to extract a portion of a string by specifying a range of indices. Here's a brief explanation using examples:


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