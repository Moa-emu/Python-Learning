#read the pdf in the folder to learn about how to decrypt

#Below will be me importing math to use functions like math.ceil
import math,pyperclip

def decryptMessage(key, message):
    #the first thing that we need to calculate is how many columns that we need
    #We do this by dividing the length of the message by the key value
    #Although to ensure that we get a whole number we will use math.ceil to round up
    columnNum =  int(math.ceil(len(message) / float(key)))

    #below will allow us to get the number of rows, since the row number is whatever the keys value is
    rowNum = int(key)

    #Below will be how we calculate the number of shaded boxes
    # it will be the total amount of box's minus the length of the message
    shadedBoxNum = (columnNum * rowNum) - len(message)

    #each string in translatedText will reprssent a column
    translatedText = [''] * columnNum

    #below the column and row variable will help to point where in the grid the next character in the encrypted message will go:
    column = 0
    row = 0

    #below will be a for loop that makes the variable called symbol for every character in the message
    for symbol in message:
        #below will put a symbol in every single translatedText[column] space
        translatedText[column] += symbol
        #below will make it go to the next column space
        column += 1

        #below is an if statement where if there are no more columns or we are in a shaded box it will go back to the first column or next row
        if (column ==  columnNum) or (column == columnNum - 1 and row >= rowNum - shadedBoxNum):
            column = 0
            row += 1

    #below will take the finished translatedText string and a join/put it in  a string to output
    return ''.join(translatedText)
    



def main():
    userMessage = input('Please put the message that you want to decrypt:')
    userKey = input('what is your key: ')

    #below will call the decryptMessage function
    translatedString = decryptMessage(userKey, userMessage)

    #Below will print the result of the translated string
    print(f'Here is your decrypted text: {translatedString}|')
    pyperclip.copy(translatedString)
 





#below will just allow our main funciton to work
if __name__ == "__main__":
    main()
