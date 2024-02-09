#This was exercise 89

# Many people do not use capital letters correctly, especially when typing on small
# devices like smart phones. In this exercise, you will write a function that capitalizes
# the appropriate characters in a string. A lowercase “i” should be replaced with an
# uppercase “I” if it is both preceded and followed by a space. The first character in
# the string should also be capitalized, as well as the first non-space character after a
# “.”, “!” or “?”. For example, if the function is provided with the string “what time
# do i have to be there? what’s the address?” then it should return the string “What
# time do I have to be there? What’s the address?”. Include a main program that reads
# a string from the user, capitalizes it using your function, and displays the result.

def correctGrammer(usersInput):
     #below will turn any lower case i by itself into capital I
     corrected_text = usersInput.replace(' i ', ' I ')

     #below will make sure that the first character in a string is capitalized
     # in further explanation it capitalizes the first charcter 
     #the + corrected_text[1:] adds the rest of the unaffected characters, further explanation (second charcter onwards)
     corrected_text = corrected_text[0].upper() + corrected_text[1:]


     # Iterate over the string to find punctuation marks and capitalize the following character
     PUNCTUATION = '.!,?'
     
     #below will use the punction variable to see if the the punction is in the Punction constant
     for punctuation in PUNCTUATION:
        #below actually finds the punctuation
        index = corrected_text.find(punctuation)
        #below makes sure that the punctation is not at the end because it needs to be there
        while index != -1:
            #below we add 3 to check whether the character following the punctuation mark is not the last character in the string (index + 3 < len(corrected_text))  and is alphabetic (corrected_text[index + 3].isalpha()).
            if index +  3 < len(corrected_text) and corrected_text[index +  3].isalpha():
                #below If the condition is true, this line capitalizes the character following the punctuation mark by slicing the string before the character, converting it to uppercase, and then concatenating it with the rest of the string.
                #below is an explanation more in detail:
                #   -corrected_text[:index + 2] takes a slice of the string up to the character just before the punctuation mark (excluding the punctuation itself).
                #   - corrected_text[index + 2].upper() converts the character immediately following the punctuation mark to uppercase.
                #   -: corrected_text[index + 3:] appends the remainder of the string, starting from the character after the one that was converted to uppercase.
                corrected_text = corrected_text[:index +  2] + corrected_text[index +  2].upper() + corrected_text[index +  3:]
            #This line updates the index to search for the next occurrence of the current punctuation mark, starting from the position right after the last found punctuation mark.
            index = corrected_text.find(punctuation, index +  1)
     
             
     
     print(corrected_text)


userText = str(input(('Whatever text that you put here will be changed to be gramatically correct:\nhell')))
correctGrammer(userText)

