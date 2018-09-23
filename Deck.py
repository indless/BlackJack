'''
A deck of Cards, 52 total, 13 of each suit
'''
#from math import random
from random import shuffle
from Card import Card

class Deck():

    def __init__(self):
        
        self.deck = []
        self.freshdeck()

    def freshdeck(self):
        '''
        Creates a fresh deck of 52 cards
        '''
        cardface = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        cardvalues = [2,3,4,5,6,7,8,9,10,10,10,10,1]
        cardsuits = ['S','C','D','H']

        cardfaceandvalues = [(cardface[i],cardvalues[i]) for i in range(len(cardface))]

        self.deck = []

        # insert a Card object for each suit,face,value combination into the deck
        
        for suit in cardsuits: 
            for face, value in cardfaceandvalues:
                self.deck.append(Card(suit,face,value))
            #for face in cardface: 
            #    for value in cardvalues:

        # shuffle the deck
        self.shuffle()

    def shuffle(self):
        '''
        Shuffle deck using shuffle function from random module
        '''
        shuffle(self.deck)

        #randomdeck = []
        #for num in range(len(self.deck)):
        #    randomdeck.append(self.deck[num])
        #    self.deck[num]

    def nextcard(self):
        '''
        Pops a Card from the deck
        If the deck has < 20 Cards left, creates a new shuffled deck
        '''
        if len(self.deck) < 20:
            self.freshdeck()
        return self.deck.pop()

