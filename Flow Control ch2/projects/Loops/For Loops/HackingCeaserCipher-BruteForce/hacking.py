#Read Information.txt and below is how we will brute force the Ceaser Cipher

#The program will decrypt the ciphertext with all possible keys
#This program will use a double for loop

print('This is the Ceaser Cipher Brute Force Decrypter')
#below will be where we store the users message
userMessage = str(input('type the ciphertext you want to decrypt: '))
#below will be a constant to keep all symbols
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

#below will be a for loop to use every possible key
#we set the range to the length of the symbols string because of the nature of how a ceaser cipher works
for key in range(len(SYMBOLS)):
    #below will keep the translated string
    #really important that it is here in the code so that it is reset every iteration  otherwise,the text that was decrypted with the current key will be added to the decrypted text in translated fromthe last iteration in the loop.
    translated = ''


    #the rest of the program is just like the ceaser cipher program


    #Below will be a for loop that we will use to iterate through all the characters of the userMessage
    # Only symbols in the symbol string can be Decrypted
    # symbol variable represents each individual character in the user's message.
    for symbol in userMessage:
     #below will be an if statement if the symbol is in the SYMBOLS CONSTANT
        if symbol in SYMBOLS:
            #below we will use the find() method to find the index in the SYMBOLS CONSTANT where symbol is
            symbolIndex = SYMBOLS.find(symbol)
            
         
            #below will subtract the key to each character in the symbol index to decrypt it
            #this is moving the found (translatedIndex)character to a diffrent position to decrypt
            translatedIndex = symbolIndex - key  
                                                                  
            
        #below will handle wraparound.....(explanation)=> When the shift reaches the end of the SYMBOLS string, it needs to "wrap around" to the beginning of the string again.  
        if translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        #below will add each translated character to the empty translated string to store the encrypted/decrypted message
        #it takes the position of the translatedIndex to take its corresponding new SYMBOL CHARACTER FROM THE SYMBOL CONSTANT
        translated = translated + SYMBOLS[translatedIndex]

    

     #below will be an else statement if the symbol is not in the SYMBOLS CONSTANT
    else:
       #the code below just adds the symbol not in the SYMBOL CONSTANT at the end of the translated string
        translated = translated + symbol


    #below will print evry possible decryption
    print(f'Key #{key}: {translated}')
 
