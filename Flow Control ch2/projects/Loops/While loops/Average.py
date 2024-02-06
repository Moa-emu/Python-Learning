#this is exercise 61

# In this exercise you will create a program that computes the average of a collection
# of values entered by the user. The user will enter 0 as a sentinel value to indicate
# that no further values will be provided. Your program should display an appropriate
# error message if the first value entered by the user is 0.
# Hint: Because the 0 marks the end of the input it should not be included in the
# average.
 
# Use a while loop for this problem

#below will get the users input
print("Please enter values that you want to add type 0 when done")
userSum = 0
#count will be the amount of times the user puts in a number we will subract 1 from it later so that 0 will not be included 
count = 0

while True:
    userNumadd = int(input('number to add: '))
    userSum += userNumadd
    count += 1
    if userNumadd == 0:
        #below will stop the while loop
        break  
Average = userSum / (count - 1)
#below will print the final average
print(f'here is your average: {Average}')
 
    










# here is a more improved version:
# there is nothing inherently wrong with your code; it correctly calculates the average of the numbers entered by the user until they enter 0. However, there are a few improvements and considerations you might want to make:

# Check for Zero Immediately: You should check if the first input is 0 immediately after reading it, rather than waiting until after the addition to the sum. This ensures that 0 is not added to the sum and counted.
# Handle Division by Zero: When calculating the average, you should handle the case where count is 0 to avoid division by zero.
# Variable Naming: It's good practice to name variables in a way that describes their purpose. Instead of userNumadd, you could use current_number.
# User Experience: Inform the user if they entered 0 as the first number, as per the requirement.
# Here's an updated version of your code with these considerations applied:

# print("Please enter values that you want to add, type  0 when done")
# userSum =  0
# count =  0

# while True:
#     current_number = int(input('Number to add: '))
#     if current_number ==  0:
#         if count ==  0:
#             print("Error: The first number entered was  0.")
#             break
#         else:
#             break
#     userSum += current_number
#     count +=  1

# if count >  0:
#     Average = userSum / count
#     print(f'Here is your average: {Average}')
# else:
#     print("No numbers were entered.")


