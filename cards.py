#Deals a random poker hand

# cards.py
#
# List and class example simulating playing cards.
#
# Cards are assigned values as follows:
# 1=A, 2-10, 11=J, 12=Q, 13=K
# There are 52 cards, 13 each in Hearts, Diamonds, Spades, and Clubs




import random

class Cards:
    def __init__(self):
        # constructor: creates a deck of cards
        
        self.deck = list(range(52))      # makes a deck of 52 cards
        # set all cards to false
        for card in self.deck:
            self.deck [card] = False;
        self.count = 0                   # counts number of cards used
        
    def getCount (self):
        # access function to return current count
        
        return self.count
        
    def dealCard (self):
        # method to randomly select a card from the deck;
        # if a card has already been selected, it may not be chosen again
        
        if self.count < 52:
            card = random.randint(0,51)         # INCLUSIVE
            # check if card has been used before and get another
            while self.deck[card] == True:
                card = random.randint(0, 51)
            # card has been "taken"
            self.deck[card] = True
            self.count = self.count + 1
            # print ("card number", self.count, "is", card)
        else:
            print ("All the cards have been dealt")
        
    def showCard (self, value, suit):
        # method to display one card in nice way
        
        if value == 1:
            face = "Ace"
        elif value == 11:
            face = "Jack"
        elif value == 12:
            face = "Queen"
        elif value == 13:
            face = "King"
        else:
            face = value
            
        print (face, "of", suit)
        

    def displayCards (self):
        # method to display all cards dealt so far
        
        for card in range (52):
            if self.deck[card] == True:
                # print (card)
                if card < 13:
                    value = card + 1
                    suit = "Hearts"
                elif card < 26:
                    value = card - 12
                    suit = "Diamonds"
                elif card < 39:
                    value = card - 25
                    suit = "Clubs"
                else:
                    value = card - 38
                    suit = "Spades"
                self.showCard (value, suit)
                

def main ():
    deck = Cards()
    while deck.getCount () < 52:
        deck.dealCard()
    
    # can now play game or whatever
    newdeck = Cards()
    for i in range (5):
        newdeck.dealCard()
        
    print()
    print ("Your poker hand is:")
    print()
    newdeck.displayCards()
main()