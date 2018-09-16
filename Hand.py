'''
A hand in BlackJack
'''
from BlackJack.card import Card

class Hand():

    def __init__(self,card=Card()):
        self.cards = [card]
        self.value = 0
        self.stay = False
        self.aces = 0
        self.bust = False
        #self.double = False
        #self.split = False


    def set_stay(self):
        '''
        Player stays, does not receive any additional cards
        '''
        self.stay = True


    def hit(self,card=Card()):
        '''
        Player hits hand, hand appends another card
        '''
        #Add card to hand
        self.cards.append(card)
        
        #keep count of aces in hand
        if card.face == 'A':
            self.aces +=1

        #update hand value
        self.value()


    def get_value(self):
        '''
        Determine value of the hand
        '''
        #adds value of each card in hand
        for card in self.cards:
            self.value += card.value

        #if hand has more than one ace, count each subsequent ace as 1
        if self.aces > 1:
            self.value -= (self.aces -1) * 10

        #if hand value over 21, hand busts
        if self.value > 21:
            self.bust = True

        return self.value


    def get_bust(self):
        '''
        return if hand has bust
        '''
        return self.bust


    def double(self,card=Card()):
        '''
        Player doubles hand, hand adds one final card and stays
        '''
        self.hit(card)
        self.stay()


    def split(self):
        '''
        Player splits hand, taking each card and creating a new hand
        Hand must have only two cards that are the same face
        '''
        if self.cards[0].face == self.cards[1].face:
            #return two hands, each containing one of the two original cards
            return Hand(self.cards[0]), Hand(self.cards[1])
