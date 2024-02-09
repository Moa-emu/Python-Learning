#here is what you can do to replace things in python 
#ex:

def correctGrammer(usersInput):
    #will replace lower case i with cow
    corrected_text = usersInput.replace('i', 'cow')
    print(corrected_text)

userText = input('write some text I will show you something cool: \n')
correctGrammer(userText)