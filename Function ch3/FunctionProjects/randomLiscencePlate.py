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

            while True:
                # This line creates a string named front. this by selecting four characters randomly from a predefined constant ALPHABET
                # The join() method is used to concatenate these characters into a single string without any separator between them because an empty string ('') is passed as the separator
                front = ''.join(random.choice(ALPHABET) for i in range(4))
                back = ''.join(random.choice(NUMBERS) for i in range(3))

                #below will make sure that the newer lisence plate 
                if len(front) ==  4 and len(back) ==  3:
                     #below will add front and back to get the newer liscnence
                    newerLicense = front + back
                    print(f'Here is your newer license plate: {newerLicense}')
                    break

                 
         





         elif userChoice == 'older':
              #below will be where we store the newer lisence plate
            newerLiscence = ''
            ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
            NUMBERS = '1234567890'
            #below will be where we will keep the characters for the front and back of the lisence plate
            front = ''
            back = ''
            
            #The while loop below will keep adding random numbers and letters and then join them together for 
            while len(front)!= 4 and len(back)!= 3:

                #below will be to add numbers to front
                #always make sure that when using len on list or string add -1 to include last item
                #below randomNum indexes a random number from the length of numbers string
                randomNum = random.randint(0, len(NUMBERS)-1)
                #below uses that random number to index a random number from numbers string 
                #now that I am looking at it this could be way simpler
                ranNumber = NUMBERS[randomNum]
                #below actually adds the number to front
                front += ranNumber

                #below will be to add letters to back
                #always make sure that when using len on list or string add -1 to include last item
                randomLetter = random.randint(0, len(ALPHABET)-1)
                #below uses the random letter number to index a letter from alphabet string
                ranLetter = ALPHABET[randomLetter]
                #below actually adds the letter to back
                back += ranLetter


                #below will add front and back to get the Older liscnence
                olderLiscence = front + back
            print(f' Here is your Older Lisence plate : {olderLiscence}')
            #break stops the loop
            break
         
         else:
             print('Invalid input please try again.')





if __name__ == "__main__":
    main()
    
