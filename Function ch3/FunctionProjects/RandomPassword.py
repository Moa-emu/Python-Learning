#below is exercise 94

# Write a function that generates a random password. The password should have a
# random length of between 7 and 10 characters. Each character should be randomly
# selected from positions 33 to 126 in the ASCII table. Your function will not take
# any parameters. It will return the randomly generated password as its only result.
# Display the randomly generated password in your file’s main program. Your main
# program should only run when your solution has not been imported into another file.

#below will allow us to use the random module
import random

def main():
     #below will be 
     SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
     #below will be a random number for the length of the password since it needs to be between 7 - 10 characters
     passwordLength = random.randint(7,10)
     password = ''.join(random.choice(SYMBOLS) for i in range(passwordLength)) 
     print(f'This is your password: {password}')


print('Hello I will create a random password for you:')
if __name__ == "__main__":
    main()

#Below will be the way that you can do this code using an ASCII range
 # Define the ASCII range for the characters to be included in the password
        #ascii_range = string.printable[:100]  # From space (ASCII  32) to tilde (ASCII  126)
    
 # Generate a random length between  7 and  10
        #password_length = random.randint(7,  10)
    
 # Generate the password by randomly choosing characters from the defined ASCII range
        #password = ''.join(random.choice(ascii_range) for _ in range(password_length))