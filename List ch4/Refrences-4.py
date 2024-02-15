#REFRENCES & PASSING REFRENCES 
#   -The premise of this topic is that when you assign a list to a variable
#    you are not act ually assigning a list to the variable. You are assinging
#    a list refrence to the variable.

# WHAT IS A REFRENCE: This is a value that points to some bit of data, a list
#                     refrence is a value that points to a list

#Below is an example to make it easier to understand

mountains = ['Everest', 'Kilamingaro', 'Fuji', 'Rocky Mountains', 'Andes']

#below I will assign mountains t oanother variable
mountainRanges = mountains

#now I will change mountain ranges
mountainRanges[0] = 'St.Helen'

# you will see now that both mountainRanges and mountains are both affected
print(mountainRanges) #prints: ['St.Helen', 'Kilamingaro', 'Fuji', 'Rocky Mountains', 'Andes']
print(mountains) #prints: ['St.Helen', 'Kilamingaro', 'Fuji', 'Rocky Mountains', 'Andes']

#THE MAIN TAKE AWAY IS THAT IN PYTHON CHANGING A REFRENCE ALSO CHANGES THE ORIGINAl
# you can do this to List and Dictionaries 






#Passing Refrences
# In Python, when you pass a list or a dictionary to a function,
# you are actually passing a reference to the object, 
#not a copy of the object itself. This means that if you 
#modify the list or dictionary within the function, 
#those changes will be reflected outside the function as well .


# Here are some examples to illustrate this concept:
# Passing a List by Reference:

def add_element(lst):
    lst.append("new element")

my_list = ["original element"]
add_element(my_list)

print(my_list)  # Output: ['original element', 'new element']
# In the example above, the add_element function receives a reference to my_list. When it appends a new element to lst, it's actually modifying the original list, and this change is reflected in my_list after the function call.



#Below demonstrates for Dictionaries which we will  go over in the next chapter
def update_info(info):
    info["address"] = "123 Main St"
    info["phone"] = "555-1234"

contact_info = {"name": "John Doe"}
update_info(contact_info)

print(contact_info)  # Output: {'name': 'John Doe', 'address': '123 Main St', 'phone': '555-1234'}

# Similarly, the update_info function receives a reference to the contact_info dictionary. It adds new key-value pairs to the dictionary, and these changes persist in the original dictionary after the function call.
# This behavior is crucial to understand because it allows for efficient manipulation of large data structures without the overhead of copying the entire structure. However, it's also important to be aware of this behavior to avoid unintentional side effects when working with mutable objects 