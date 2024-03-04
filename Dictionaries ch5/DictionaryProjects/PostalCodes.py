#This is exercise 132

# In a Canadian postal code, the first, third and fifth characters are letters while the
# second, fourth and sixth characters are numbers. The province can be determined
# from the first character of a postal code, as shown in the following table. No valid
# postal codes currently begin with D, F, I, O, Q, U, W, or Z.

# Province                  First character(s)
#-----------------------------------------------
# Newfoundland          |    A
# Nova Scotia           |    B
# Prince Edward Island  |    C
# New Brunswick         |    E
# Quebec                |    G, H and J
# Ontario               |    K, L, M, N and P
# Manitoba              |    R
# Saskatchewan          |    S
# Alberta               |    T
# British Columbia      |    V
# Nunavut               |    X
# Northwest Territories |    X
# Yukon                 |    Y


# The second character in a postal code identifies whether the address is rural or
# urban. If that character is a 0 then the address is rural. Otherwise it is urban.
# Create a program that reads a postal code from the user and displays the province
# associated with it, along with whether the address is urban or rural. For example,
# if the user enters T2N 1N4 then your program should indicate that the postal code
# is for an urban address in Alberta. If the user enters X0A 1B2 then your program
# should indicate that the postal code is for a rural address in Nunavut or Northwest
# Territories. Use a dictionary to map from the first character of the postal code to the
# province name. Display a meaningful error message if the postal code begins with
# an invalid character.




#Below will be a dictionary that will hold all of the key press data
PostalCodes ={
    'Newfoundland':'A',
    'Nova Scotia':'B',
    'Prince Edward Island': 'C',
    'New Brunswick': 'E',
    'Quebec':'GHJ',
    'Ontario':'KLMNP',
    'Manitoba':'R',
    'Saskatchewan':'S',
    'Alberta':'T',
    'British Columbia':'V',
    'Nunavut':'X',
    'Northwest Territories':'X',
    'Yukon':'Y'
}

 
    




def FindPostal():
    

    #Below will capture the users text
     
    askUser = str(input('Please type a postal code and we will tell you wheather it is urban or rural and where it is: '))
    #Below will be a flag if a match is found
    found = False
    
    #below will make all the letters the user types 
    upperaskUser = askUser.upper()
    #below will go through all of the keys and values in the postal Codes dictionary
    for key,value in PostalCodes.items():
        #below will check if the fist character corelates with any values in the dictionary
        # we use in instead of == because of cases like qubec: 'GHJ'
        if upperaskUser[0] in value:
            print(f'This is a rural adress in {key}')if upperaskUser[1] == '0' else print(f'This is a Urban adress in {key}') 
            found = True
            break

    #If no match was found, execute the else block
    if not found:
        print('The postal code entered does not match any known codes.')
    
             
         


def main():
    FindPostal()

if __name__ == "__main__":
    main()
