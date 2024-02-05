#Conditionals - allow your program to make decisions based upon if certain parts of your program are true or not
#REMBMER TO INDENT YOUR CONDITIONALS

#There are three conditionals

#if statements - meaning it will execute code if the statement is true
#elif statements - these are just basically extra if statements 
#else statements are followed by if statements and only run code if the if statement is false

#here is an example below
#you can draw a if, elif and else flowchart to demonstrate
number = 15

if number > 20:
    print("The number is greater than 20.")
elif number > 10:
    print("The number is greater than 10 but not greater than 20.")
else:
    print("The number is not greater than 10.")