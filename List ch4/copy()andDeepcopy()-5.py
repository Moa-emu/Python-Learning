#COPY() AND DEEPCOPY


# In Python, copy() and deepcopy() are functions from the copy module that 
#are used to create copies of objects. Both of these functions are used to 
#duplicate objects, but they differ in how they handle the copying of 
#compound objects like lists and dictionaries 234.




# copy(): Shallow Copy
# A shallow copy of a list creates a new list object, but fills it with references to the objects found in the original list. In other words, a shallow copy duplicates the top-level structure of the list but doesn't duplicate the objects themselves. If the original list contains mutable objects (like lists or dictionaries), and you modify those objects, the changes will be visible in the copied list because they share references to the same objects 234.
# Here's an example of using copy() to create a shallow copy of a list:
import copy

original_list = [[1], [2]]
shallow_copy = copy.copy(original_list)

# Modify the original list
original_list[0][0] =  100

print(original_list)      # Output: [[100], [2]]
print(shallow_copy)       # Output: [[100], [2]]
print(id(original_list))  # Output: Some ID
print(id(shallow_copy))   # Output: Different ID, but points to the same sublists






# deepcopy(): Deep Copy
# A deep copy, on the other hand, creates a new list object and recursively
# inserts copies of the objects found in the original list. This means that 
#changes to the original list or the objects it contains won't affect the 
#deep copied list 234.
# Here's an example of using deepcopy() to create a deep copy of a list:
import copy

original_list = [[1], [2]]
deep_copy = copy.deepcopy(original_list)

# Modify the original list
original_list[0][0] =  100

print(original_list)      # Output: [[100], [2]]
print(deep_copy)          # Output: [[1], [2]]
print(id(original_list))  # Output: Some ID
print(id(deep_copy))      # Output: Different ID, and contains different sublists





# The choice between using copy() and deepcopy() depends on whether you want
# to create a new list that shares references with the original list (copy())
# or a completely independent copy of the list (deepcopy()).
# The deepcopy() function is typically used when you need to ensure that
# changes to the original list or its contents do not affect the copied list.