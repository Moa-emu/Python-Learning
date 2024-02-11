#read the pdf in the folder to learn about how to decrypt

def decryptMessage(key, message):
    #the first thing that we need to calculate is how many columns that we need
    #We do this by dividing the length of the message by the key value
    #Although to ensure that we get a whole number we will use math.ceil to round up
    
    



def main():
    userMessage = input('Please put the message that you want to decrypt')
    userKey = input('what is your key: ')

    #below will call the decryptMessage function
    decryptMessage(userKey, userMessage)



    #Below will print the users decrypted message
    print('Here is your decrypted message: ')





#below will just allow our main funciton to work
if __name__ == "__main__":
    main()
