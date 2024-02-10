#read up on the transposition cipher and the code below will do what we need

#below we are importing pyperclip so that we can copy the ciphertext there

#below will be our def main() function
def main():
    #below the user will put the message they want to encrypt
    userMessage = str(input('please put the message that you want to encrypt: '))
    #below will be the key that the user wants to use
    userKey = int(input('Type the key value you would like to use:'))



#below will be a function that actualy encrypts the text
    #below the function takes the key and messge arguments
    def encryptMessage(key, message):
        #below will contain a list data type we will learn more about this later. list take individual items/elements that can be whatever data type value as long as it does not conflic with your code
        #each string in cipher text represents a column, since nthe number of columns is equal to the key the user uses
        cipherText = [''] * key

        #below will loop through each column in ciphertext
        for column in range(key):
            #below will make the currentIndex variable to whatever column num is
            currentIndex = column

            #the while finds and concatenates the right charcter in usermessage
            #below will make the while loop keep looping until currentIndex goes past the message length
            while currentIndex < len(userMessage):
                #below will place the charcter at currentIndex in message at the end of the current column in the ciphertext list
                cipherText[column] += message[currentIndex]

                #below moves curent index over:
                currentIndex += key


