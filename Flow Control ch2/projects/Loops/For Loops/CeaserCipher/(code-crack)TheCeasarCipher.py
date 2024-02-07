#read the text file explaining the ceaser Cipher 
# for this project we will be using import statements, constants, for loops, conditions, in and not in and the find string method


#below I am importing pyperclip module
#pyperclip will allow us to use functions like pyperclip.copy()
#pyperclip.copy() will allow us to automatically copy string to your computer's clipboard so that you can convieniently paste them into other programs
import pyperclip # i had to pip install this


#Below is a prompt
print('Hello this is a ceaser cipher encrypter and decripter all you have to do is type message, put key number and say wheather you want to encrypt or decript')

#below will be the users message
userMessage = input('what is your message: ')

#Below will be the encryption/ decryption key
userKey = int(input('what is your key: '))

#below will be a while loop that make sure the user chooses between ecrypting or decrypting
userChoice = str(input('what mode would you like type(encrypt or decrypt):'))

# if the user does not type encrypt and decrypt it will tell them to put the correct response
while userChoice != 'encrypt' and userChoice != 'decrypt':
    print('please type a correct response, try again')
    #below I am calling the user choice variable to ask again
    userChoice = str(input('what mode would you like type(encrypt or decrypt):'))


#Below will be a constant(variable that does not change) we need it so that it  contains every possible character that can be encrypted with this Caesar cipher. Because that string shouldn’t change, we store it in the constant variable
#Symbol is a common term used in cryptography for a single character that a cipher can encrypt or decrypt. A symbol set is every possible symbol a cipher is set up to encrypt or decrypt.
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'


# translated will store the encrypted/ decrypted  form of the usersMessage
translated = ''


#Below will be a for loop that we will use to iterate through all the characters of the userMessage
# Only symbols in the symbol string can be encrypted/Decrypted
# symbol variable represents each individual character in the user's message.
for symbol in userMessage:
     #below will be an if statement if the symbol is in the SYMBOLS CONSTANT
    if symbol in SYMBOLS:
        #below we will use the find() method to find the index in the SYMBOLS CONSTANT where symbol is
        symbolIndex = SYMBOLS.find(symbol)
        
        #after finding where it is we can navigate wheather to encrypt or decrypt based on users choice
        if userChoice == 'encrypt':
            #below will add the key to each character in the symbol index to ecrypt it
            #this is moving the found (translatedIndex)character to a diffrent position to encrypt
            translatedIndex = symbolIndex + userKey

        elif userChoice == 'decrypt':
            #below will subtract the key to each character in the symbol index to decrypt it
            #this is moving the found (translatedIndex)character to a diffrent position to decrypt
            translatedIndex = symbolIndex - userKey


        #below will handle wraparound.....(explanation)=> When the shift reaches the end of the SYMBOLS string, it needs to "wrap around" to the beginning of the string again. Similarly, if the shift goes beyond the start of the string, it should go to the end of the string instead.
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        #below will add each translated character to the empty translated string to store the encrypted/decrypted message
        #it takes the position of the translatedIndex to take its corresponding new SYMBOL CHARACTER FROM THE SYMBOL CONSTANT
        translated = translated + SYMBOLS[translatedIndex]

    

     #below will be an else statement if the symbol is not in the SYMBOLS CONSTANT
    else:
       #the code below just adds the symbol not in the SYMBOL CONSTANT at the end of the translated string
        translated = translated + symbol


#below will just output the translated string
if userChoice == 'encrypt':
    print(f'here is your encrypted message: {translated}')
elif userChoice == 'decrypt':
    print(f'here is your decrypted message: {translated}')
#below will copy the translated message in the users sticky note app
pyperclip.copy(translated)
         
