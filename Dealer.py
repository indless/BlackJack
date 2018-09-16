'''
Dealer is a player and uses Deck
'''
import deck
import hand

class Dealer():

    def __init__(self,deck=Deck(),hand=Hand()):

        self.deck = deck
        self.dealerhand = hand

    def deal(self):
        self.deck.nextcard()
