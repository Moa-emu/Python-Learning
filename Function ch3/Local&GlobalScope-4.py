#LOCAL AND GLOBAL SCOPE 
#NOTE YOU DO Not need to really understand/Explain this part
#local scope - any parameters and variables assigned in a called function
#global scope - any variables outside all functions 
#below are reasons why this matters
#   -Code in the global scope cannot use any local variables.
#   -However, a local scope can access global variables.
#   -Code in a function’s local scope cannot use variables in any other local scope.
#   -You can use the same name for different variables if they are in different scopes. That is, there can be a local variable named spam and a global variable also named spam.
#REMEMBER DO NOT RELY ON GLOBAL VARIABLES IN YOUR PROGRAMS USE THEM SPARINGLY
#remember -local variables in one function are seprate from local variables in another
#always give your variables diffrent names throught program as to not get confused
#below is some more explanation if you need it


# Local Scope: A variable with local scope is defined inside a function. It is only accessible within that function and is created when the function starts executing. Once the function ends, the local variable is destroyed. An example of a local variable is shown below:
def my_function():
    local_var = "I'm local!"
    print(local_var)

my_function()  # Prints: I'm local!
#print(localvar) <=# Raises an error because local_var is not defined in this scope






# Global Scope: A variable with global scope is defined outside of all functions and is accessible anywhere in the program, both inside and outside functions. Global variables persist for the lifetime of the program. Here's an example:
global_var = "I'm global!"

def my_function():
    print(global_var)

my_function()  # Prints: I'm global!
print(global_var)  # Also prints: I'm global!







# If you want to modify a global variable inside a function, you must use the global keyword:
global_var = "Original value"

def modify_global():
    global global_var
    global_var = "Modified value"

modify_global()
print(global_var)  # Prints: Modified value
# By declaring global_var as global within the function, you're telling Python that you intend to use the global variable named global_var, rather than creating a new local variable with the same name