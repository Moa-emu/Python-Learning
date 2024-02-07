# The reverse cipher encrypts a message by printing it in reverse order. So “Hello, world!” encrypts to
# “!dlrow ,olleH”. To decrypt, or get the original message, you simply reverse the encrypted message.
# The encryption and decryption steps are the same.

print('hello mr.spy type the phrase you want us to reverse:')
userString = str(input())

# below I am going to initialize i to be the end of the string
i = len(userString)-1
#reversed word is where we will keep the string
reversedWord = ''

# we make sure that while loop stops at 0 since that is the beggining of the string
while i >= 0:
    #below will get the current character
    word = userString[i]
    #below will add the current charcter to reversed word
    reversedWord += word
    #below will decrease i so that it can keep moving to the beggining of the string
    i = i -1 #or you could do i -= 1
print(reversedWord) 