#While Loops in python are statements that allow you to execute a block of code again and again as long as the condition is true
#below is an example of a while loop
greeting = 0
while greeting < 5:
    print('hello world')
    greeting = greeting + 1
#below the everytime the while loops runs it increases 1 untile the condition is no longer true and the loop stops




#below is a simple program that shows another use of while loops
print('please create a password:')
createdPassword = input()
print('now please enter the password you created')
answer = input()
#it will keep asking the user for the password until it is correct
while answer != createdPassword:
    print('incorect password try again')
    print('enter the password you created: ')
    answer = input()
print('that is the correct password thank you!')


#BEWARE OF INFINITE LOOPS WHERE  YOUR WHILE LOOP IS ALWAYS TRUE AND IT KEEPS GOING FOREVER


#BREAK STATEMENTS - these are a way to break out of a while loop
#ex: below
count = 0
while True:
    print(f"This is loop iteration {count}")
    
    if count == 5:
        print("Breaking the loop.")
        break
    
    count += 1

print("Loop has been broken.")




#CONTINUE STATEMENTS - these are a way to jump imeadiatly back to the loop 
#the example below shows how we can use continue statements to skip even numbers
print("Let's count to 10, but skip even numbers:")
counter = 0
while counter <= 10:
    if counter % 2 == 0:
        counter += 1
        continue # Skip printing the even numbers
    print(counter)
    counter += 1




# Im skipping truthsey and falsey values in python but maybe read up on them