# This is exercise 119


# In many card games each player is dealt a specific number of cards after the deck
# has been shuffled. Write a function, deal, which takes the number of hands, the
# number of cards per hand, and a deck of cards as its three parameters. Your function
# should return a list containing all of the hands that were dealt. Each hand will be
# represented as a list of cards.
# When dealing the hands, your function should modify the deck of cards passed
# to it as a parameter, removing each card from the deck as it is added to a player’s
# hand. When cards are dealt, it is customary to give each player a card before any
# player receives an additional card. Your function should follow this custom when
# constructing the hands for the players.
# Use your solution to Exercise 118 to help you construct a main program that
# creates and shuffles a deck of cards, and then deals out four hands of five cards each.
# Display all of the hands of cards, along with the cards remaining in the deck after
# the hands have been dealt.

import random

def createDeck():
    #below will hold all of the cards  
    cardDeck = []
    cardSuit = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    specialCharacters = ['Ace', 'Ten', 'Jack', 'Queen','King', '2','3','4', '5','6','7','8','9']

    # i represents each individual element in cardSuit
    # x represents each individual element in specialCharacters
    for i in cardSuit:
        for x in specialCharacters:
            #print(f'{x} of {i}') #this prints all of the charcters
            cardDeck.append(f'{x} of {i}')
            
    print(cardDeck)
    #Below will allow us to return the cardDeck variable to another function
    return(cardDeck)
    #below I am just checking that there are 52 cards in the deck
    #print(len(cardDeck))


def shuffleCards(cardsDeck):
    #below will randomly shuffle the list
    random.shuffle(cardsDeck)
    print(cardsDeck)


def deal(shuffledCards):


    print('hello')


def main():
     
    while True:
        print('1.) Shows unshuffled cards\n2.)Shows shuffled cards\n3.)Deals cards\n4.)goes back')
        askUser = input('Type the number of choice do you want to make: ')

        if askUser == 1:
            print('hello')
        
        if askUser == 2:
            print('2 is ')

        if askUser == 3:
            print('there are')

        if askUser == 4:
             continue

        else:
            print('invalid input')
        


    print('Here is a unshuffled deck of cards:')
    unshuffledCardDeck = createDeck()
    print('The cards have now been shuffled here it is:')
    shuffleCards(unshuffledCardDeck)
    


if __name__ == "__main__":
    main()
