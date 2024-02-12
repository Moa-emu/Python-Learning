# To ensure the reliability of transposition cipher programs for encryption and decryption, extensive manual testing with various messages and keys can be time-consuming and tedious. Instead, an automated testing program can be written to generate random messages and keys, which are then encrypted and decrypted using the cipher programs. Automated testing allows for the rapid execution of numerous combinations, confirming the functionality of the encryption and decryption processes 


#below will be the libraries that we will import
#I also made some copies I did of the encrypt and decrypt programs that I made
import random, sys, DecryptTranspositionCopy, EncryptingWithColumnarTranspositionCipherCopy

def main():
    #below we will be seeding a random number then using the random.randint.
    #the difference is that when you seed you get a pseudo random number it is not really random and you can predict the pattern
    #without seeding you will get an actual random number
    random.seed(42)# seeding random numbers is good for testing your programs because you want predictable numbers so the same pseudorandom messages and keys are chosen


    #Below will be a for loop that will fun 20 test 
    for i in range(20):

        #below will generate random messages to test
        #we will be multiplying the message string by a random number, think like this 'ABC' * 3 = 'ABCABCABC'
        #then after multiplying later down we will shuffle that string to have more random text
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' * random.randint(4, 40)

        #below will convert the message into a list we will go over list more in the next chapter
        message = list(message)
        #below will use the random.shuffle() function to shuffle all of the elements in the list in a random way
        random.shuffle(message)

        #below will convert the message list back into a string
        message = ''.join(message)


        #Below will be how we test each message
        #______________________________________________________________________________________________________
        #this will just print what we are testing# also REMBER THAT WE ARE STILL IN A FOR LOOP
        #notice in message how we use message[:50] will give us the first 50 characters
        #we use i+1 so that we start with 1 instead of 0 because all things in programming start with 0 
        print(f'Test #{i+1}: {message[:50]}')


        #below will check all possible keys for each message since there are only as many keys as there characters in the message which is why we use len(message)
        #but we divide it by 2 to limit the amount of  keys that we will have to test
        for key in range(1, int(len(message)/2)):
            #below we will be calling the functions from the other files to use them
            encrypted = EncryptingWithColumnarTranspositionCipherCopy.encryptMessage(key, message)
                    #we put the encrypted variable above as one of the parameters for decrypted
            decrypted = DecryptTranspositionCopy.decryptMessage(key, encrypted)

            #below if the decryption does not match the original message then we display an error message and quit
            if message != decrypted:
                print(f'Mismatch with key {key} and message: {message}')
                print(f'Decrypted as: {decrypted}')
                sys.exit()
    
    #below is an else statement if everything in the for loop is good
    else:
        print('Transposition cipher test passed')
 

#if test.py is run(instead of imported as a module) call the main() function
if __name__ == '__main__':
    main()


#Below is hwo we can test this test program:
# We’ve written a program that tests the transposition cipher programs, but how do we know that the
# test program works? What if the test program has a bug, and it just indicates that the transposition
# cipher programs work when they really don’t?
# We can test the test program by purposely adding bugs to the encryption or decryption
# functions. Then, if the test program doesn’t detect a problem, we know that it isn’t running as
# expected.
# To add a bug to the program, we open transpositionEncrypt.py and add + 1 to line 36:
# transposition
# Encrypt.py
# 35. # Move currentIndex over: it replaces currentIndex += key
# 36. currentIndex += key + 1
# Now that the encryption code is broken, when we run the test program, it should print an error,
# like this: