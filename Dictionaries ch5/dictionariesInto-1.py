# EXPLAINING THE DICTIONARY DATA TYPE 

#similar to list dictionaries hold many diffrent data types but the only
#differences between them is list use indexes while dictionaries use keys
#which are associated with key-value pairs.
# syntax for a dictionary => dictionaryName = {key:value, key:value}
#Below is an example: 
Friren = {'Race':'Elf', 'Age':'over 1,000 years old', 'Personality':'relaxed'}

#below is how you will get a value out of a dictionary 
print(f"Frierens personality is: {Friren['Personality']}")

#NOTE REMEMBER THAT DICTIONRY KEYS DO NOT START AT 0 DICTIONARIES ARE UNORDERED IT DOES NOT MATTER WHAT ORDER THINGS ARE ARANGED
# you can also use intergers as keys
#example below:
AriAstersMovies = {1:'Keeping Up with the Johnsons', 2:'Hereditary', 3:'Midsommer', 4:'Beau is Afraid'}

#you can also do comparisons with dictionaries to show that 
scariestMovies = {'name': 'heriditary', 'name2':'the witch'}
Movies = { 'name2':'the witch','name': 'heriditary'}
print(scariestMovies == Movies) # this prints true
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Below is an example of using dictionaries in a program
contries = {'America':'341,139,019', 'China':'1,425,360,912' , 'Nigeria':'227,091,386', 'India':'1,436,840,066' , 'Pakistan':'243,433,741' , 'Indonesia':'278,966,829'}

while True:
    print('type 0 when you are done')
    userInput = input('Type a Country and we will return the countries population:  ')
    if userInput == '0':
        break
    else:
        if userInput in contries:
            print(f"The population of {userInput} is {contries[userInput]}")
        else:
            print('That country is not in our database')

