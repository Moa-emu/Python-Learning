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








#if test.py is run(instead of imported as a module) call the main() function
if __name__ == '__main__':
    main()