#exercise 95

# In a particular jurisdiction, older license plates consist of three letters followed by
# three numbers. When all of the license plates following that pattern had been used,
# the format was changed to four numbers followed by three letters.
# Write a function that generates a random license plate. Your function should have
# approximately equal odds of generating a sequence of characters for an old license
# plate or a new license plate. Write a main program that calls your function and
# displays the randomly generated license plate.

#below we are importing random so that we can use it
import random

def main():
    while True:
         userChoice = input(('type newer or older for us to randomly give you a liscence plate of that time: '))
         if userChoice == 'newer':
             #below will be where we store the newer lisence plate
            newerLiscence = ''
            ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
            NUMBERS = '1234567890'
            #below will be where we will keep the characters for the front and back of the lisence plate
            front = ''
            back = ''
            
            #The while loop below will keep adding random numbers and letters and then join them together for 
            while len(front)!= 4:
                randomNum = random.randint(0, len(NUMBERS)-1)
                randomLetter = random.randint(0, len(ALPHABET)-1)
                

                #below will be a for loop to add numbers
                ranNumber = NUMBERS[randomNum]
                front += ranNumber
            print(front)
                
                
                #below will be a for loop to add letters
                #ranLetter = ALPHABET[randomLetter]


            break
         
         elif userChoice == 'older':
             #below will be where we store the older liscence plate
            newerLiscence = ''
            ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
            NUMBERS = '1234567890'
            break
         
         else:
             print('Invalid input please try again.')





if __name__ == "__main__":
    main()
    
