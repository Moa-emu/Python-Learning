#This is Exercise 130: Text Messaging


# On some basic cell phones, text messages can be sent using the numeric keypad.
# Because each key has multiple letters associated with it, multiple key presses are
# needed for most letters. Pressing the number once generates the first letter on the
# key. Pressing the number 2, 3, 4 or 5 times generates the second, third, fourth or fifth
# character listed for that key.
# Key  Symbols
#-------------
# 1  |  .,?!:
# 2  |  ABC
# 3  |  DEF
# 4  |  GHI
# 5  |  JKL
# 6  |  MNO
# 7  |  PQRS
# 8  |  TUV
# 9  |  WXYZ
# 0  |  space

# Write a program that displays the key presses that must be made to enter a text
# message read from the user. Construct a dictionary that maps from each letter or
# symbol to the key presses. Then use the dictionary to generate and display the presses
# for the user’s message. For example, if the user enters Hello, World! then your
# program should output 4433555555666110966677755531111. Ensure that
# your program handles both uppercase and lowercase letters. Ignore any characters
# that aren’t listed in the table above such as semicolons and brackets.






#Below will be a dictionary that will hold all of the key press data
keyPressesData = {
    1:'.,?!:', 
    2:'ABC', 
    3:'DEF', 
    4:'GHI', 
    5:'JKL', 
    6:'MNO', 
    7:'PQRS', 
    8:'TUV', 
    9:'WXYZ', 
    0:' '
    }

def convertText():
    #Below will capture the users text
    askUser = input('Please type what you want to convert: ')
    result = ''
    for char in askUser:
        #Below will make a variable to store all of the uppercase characters
        char_upper = char.upper()

        #Below will get all of the keys, values from the items in the keyPressesData Dictionary
        for key, value in keyPressesData.items():
            #Below will check if the users characters are in the keyPressData values
            if char_upper in value:
                #below is to find the position of each value so we can multiply it 
                position = value.index(char_upper) + 1
                #Below will add all of the found converter characters keys in the result
                result += str(key) * position
                break
        else:
            result += char
    print(result)


def main():
    convertText()

if __name__ == "__main__":
    main()
