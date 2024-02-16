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
    return(cardsDeck)




def main():
     
    while True:
        print('1.) Shows unshuffled cards\n2.)Shows shuffled cards\n3.)Deals cards\n')
        askUser = input('Type the number of choice do you want to make: ')

        if askUser == '1':
            print('Here is your unshuffled deck of cards:')
            unshuffledCardDeck = createDeck()
        
        elif askUser == '2':
            print('The cards have now been shuffled here it is:')
            remainingCards = shuffleCards(unshuffledCardDeck)

        elif askUser == '3':
            
             
            PlayerItems = random.sample(remainingCards, 5)
            for item in PlayerItems:
                remainingCards.remove(item)

            hand2Items = random.sample(remainingCards, 5)
            for item2 in hand2Items:
                remainingCards.remove(item2)

            hand3Items = random.sample(remainingCards, 5)
            for item3 in hand3Items:
                remainingCards.remove(item3)

            hand4Items = random.sample(remainingCards, 5)
            for item4 in hand4Items:
                remainingCards.remove(item4)
            #below is a for loop that will remove each selected Item from the remaining cards list
        
            print(f'here is the PlayersHand: {PlayerItems}\n')
            print(f'here is the Hand2: {hand2Items}\n')
            print(f'here is the Hand2: {hand3Items}\n')
            print(f'here is the Hand2: {hand4Items}\n')
            print(f'here is the remaining cards in your deck: {remainingCards}\nhere is the number of cards left:{len(remainingCards)}')

            #Here is a more efficent way to do it WITH LIST SLICING:
                # import random
                 # remainingCards = [ ... ]  # Your list of cards
            # Shuffle the cards to ensure randomness
                 # random.shuffle(remainingCards)
            # Split the shuffled list into player hands
                # PlayerItems = remainingCards[:5]
                # hand2Items = remainingCards[5:10]
                # hand3Items = remainingCards[10:15]
                # hand4Items = remainingCards[15:20]
            # Ensure that the hands are separated correctly
                # remainingCards = remainingCards[20:]
             

        else:
            print('invalid input')
        


    
    
    


if __name__ == "__main__":
    main()
