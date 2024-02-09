# below is exercise 96

# In this exercise you will write a function that determines whether or not a password
# is good. We will define a good password to be a one that is at least 8 characters
# long and contains at least one uppercase letter, at least one lowercase letter, and at
# least one number. Your function should return true if the password passed to it as
# its only parameter is good. Otherwise it should return false. Include a main program
# that reads a password from the user and reports whether or not it is good. Ensure that your main program only runs when your solution has not been imported into
# another file.

def main():
    print('Create a password for your account.\nHere are the rules for Password Creation\n1.)should be atleast 8 characters long\n2.Should have at least one uppercase letter, one digit and one lower case letter')
    #below will be a while loop that will continue if the users password is bad
    while True:
        #below will ask the user for their password
        askUser = input(('Please create a Password: '))

        #Below will be if the users password meets all of the conditions
        #also we will be using the any operator which returns True if at least one element in an iterable (like a list, tuple, or set) is truthy
        if (len(askUser) >= 8) and (any(char.isupper() for char in askUser) and (any(char.isdigit() for char in askUser)) and (any(char.islower() for char in askUser))):
            print('Your password is good')
            break
        
        # the else will be all the possible scenarios that the users password does not meet the standards
        else:
            if len(askUser) < 8:
                print('your password is less than 8 characters, try again')
            if not (any(char.isupper() for char in askUser)):
                print('You have no capital letters, try again')
            if not (any(char.isdigit() for char in askUser)):
                print('you have no digits in your password, try agian')
            if not (any(char.islower() for char in askUser)):
                print('you have no lowercase letters in your password, try again')
             
        






if __name__ == "__main__":
    main()
