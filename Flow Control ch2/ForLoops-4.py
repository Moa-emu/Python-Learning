#For loops allow us to loop a value a certain number of times instead of how while loops are jsut as long as a condition is true
#   -to make a for loop  make sure you type for i in range(#number):
#   - the number that you put inside the parenthesis is how many times the loop will iterate
print('can you count how many fish there are')
fish = 1
for i in range(5):
    print(fish)
    if fish == 5:# I put this line of code here because that the final print statement is ouside of the loop so it will print the value of fish after the loop completes
        break
    fish = fish + 1
    
print('there are ' + str(fish) + ' fish there.')


#below is a way to make a while loop behave like a for loop
print('My name is')
i = 0
while i < 5:
 print('Jimmy Five Times (' + str(i) + ')')
 i = i + 1






#*end is just a way to say end with a empty string

# ARGUMENTS OF RANGE remember that range can take 3 arguments(starting value, stopping value, and stepping value)
# range(#number) - only means stop at that number
#ex: 
for i in range(5):
    print(i, end=' ')

# Output: 0 1 2 3 4



# range(#number1, #number2 )- means start at #number1 end when approaching #number2
# range with start and stop arguments
for i in range(2, 7):
    print(i, end=' ')

# Output: 2 3 4 5 6




# range(#number1, #number2, #number3)- means start at #number1 end when approaching #number2 and skip #number3 amount of times every loop
for i in range(1, 10, 2):
    print(i, end=' ')

# Output: 1 3 5 7 9
    


# you can even use  negative numbers if you wanted to count down
for i in range(10, -1, -1):
    print(i, end=' ')

# Output: 10 9 8 7 6 5 4 3 2 1 0