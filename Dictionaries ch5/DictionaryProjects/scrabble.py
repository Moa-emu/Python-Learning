#This is exercise 137

# In the game of Scrabble™, each letter has points associated with it. The total score
# of a word is the sum of the scores of its letters. More common letters are worth fewer
# points while less common letters are worth more points. The points associated with
# each letter are shown below:
# One point A, E, I, L, N, O, R, S, T and U
# Two points D and G
# Three points B, C, M and P
# Four points F, H, V, W and Y
# Five points K
# Eight points J and X
# Ten points Q and Z
# Write a program that computes and displays the Scrabble™ score for a word.
# Create a dictionary that maps from letters to point values. Then use the dictionary to
# compute the score.

#Below will be so that we can choose random numbers correlating with random words
import random

#Below will be a list that will contain random words
random_words = [
    "apple",
    "banana",
    "carrot",
    "elephant",
    "zebra",
    "computer",
    "table",
    "chair",
    "lamp",
    "sun",
    "moon",
    "star",
    "water",
    "fire",
    "earth",
    "air",
    "snake",
    "ladder",
    "book",
    "pencil",
    "paper",
    "school",
    "university",
    "student",
    "teacher",
    "doctor",
    "nurse",
    "engineer",
    "scientist",
    "artist",
    "musician",
    "writer",
    "poet",
    "painting",
    "sculpture",
    "architecture",
    "photography",
    "dance",
    "theater",
    "movie",
    "cinema",
    "popcorn",
    "soda",
    "pizza",
    "burger",
    "fries",
    "ice cream",
    "cake",
    "cookie",
    "candy",
    "chocolate",
    "strawberry",
    "orange",
    "grape",
    "pineapple",
    "watermelon",
    "kiwi",
    "lemon",
    "coconut",
    "mango",
    "peach",
    "pear",
    "plum",
    "apricot",
    "blueberry",
    "raspberry",
    "blackberry",
    "avocado",
    "broccoli",
    "cucumber",
    "lettuce",
    "tomato",
    "potato",
    "carrot",
    "onion",
    "garlic",
    "ginger",
    "pepper",
    "salt",
    "sugar",
    "flour",
    "butter",
    "oil",
    "milk",
    "cheese",
    "egg",
    "chicken",
    "beef",
    "fish",
    "shrimp",
    "rice",
    "noodle",
    "bread",
    "soup",
    "salad",
    "sandwich"
     
]

#Below will be a dictionary that will keep track of how many points each letter is worth
wordPoints = {
    1:'AEILNORSTU',
    2:'DG',
    3:'BCMP',
    4:'FHVWY',
    5:'K',
    8:'JX',
    10:'QZ'
}

#Below is a function that will pick a random word from our random_words list
def pickedWord():
    #Below will allow us to use the length of a list to pick a random word
    randomNum = random.randint(0, len(random_words)-1)
    #Below will pick a random word
    picked_word = random_words[randomNum]

    #below will return the picked word 
    return picked_word

#Below is a function that will give the total value of the the picked word  
def totalPoints(picked_word):
    total_value = 0
    
    #Below will capitilize all of the words in the picked word
    upperPickedWord = picked_word.upper()
    #below will give the total points of the picked word
    for char in upperPickedWord:
        #below will be how we go through the wordPoints dictionary
        for key, value in wordPoints.items():
            #below will check that the char is in the wordpoints dictionary values
            if char in value:
                #each time the char is in the value it will add the chars associated key 
                total_value += key
    #print(f' the word {picked_word} has the value of {total_value}')
    return total_value


def main():
    word = pickedWord()
    lengthWord = len(word)
    totalWordPoints = totalPoints(word)
    
    #below will welcome the user 
    print('Hello, we picked a random word you have to guess each letter')
    print(f'word:{word}, length:{lengthWord}, total points:{totalWordPoints}')
    #below will be a while loop that will always ask the user to guess a word
    totalscore = 0
    while True:
        print(f'total score: {totalscore}')
        askUser = str(input('Type your letter guess: '))

        #Below is just a case to stop the loop
        if askUser == 'stop':
            break


        #Below will happen if the users guess is greatr than a single letter
        while len(askUser) > 1:
            print('your guess is bigger than a single letter try again')
            askUser = str(input('Type your letter guess: '))

       
        
        if askUser in word:
            print('pretty good')
            userGuess = askUser.upper()
            if userGuess in wordPoints.values():
                print('good')
            
            
        else:
            print('not good')
        

        


    #print(f'here is the word:{word}, length:{lengthWord}, and total points{totalWordPoints}')

if "__main__" == __name__:
    main()