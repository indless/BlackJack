'''
A hand in BlackJack
'''
#from Card import Card

class Hand():

    def __init__(self,playerid=0,bet=0):
        self.cards = []
        self.playerid = playerid
        self.value = 0
        self.stay = False
        self.aces = 0
        self.blkjck = False
        self.bust = False
        self.bet = bet
        self.soft16 = False
        self.paid = False
        #self.double = False
        #self.split = False


    def set_stay(self):
        '''
        Player stays, does not receive any additional cards
        '''
        self.stay = True


    def hit(self,card):
        '''
        Player hits hand, hand appends another card
        '''
        #Add card to hand
        self.cards.append(card)
        
        #keep count of aces in hand
        if card.face == 'A':
            self.aces +=1

        #update hand value
        v = self.get_value()


    def get_value(self):
        '''
        Determine value of the hand
        '''
        self.value = 0
        
        #adds value of each card in hand
        for card in self.cards:
            self.value += card.value

        #if hand has an ace and the value of the hand is less than or equal to 11, add 10
        if self.aces > 0 and self.value <= 11:
            self.value += 10

        #determine if soft 16. primarily used for dealer hands
        if self.aces > 0 and self.value - 10 == 6:
            self.soft16 = True
        else:
            self.soft16 = False

        #if hand value over 21, hand busts
        if self.value > 21:
            self.bust = True
            self.stay = True
        
        #if hand value = 21
        if self.value == 21: 
            self.stay = True
            # and with only 2 cards, BlackJack!
            if len(self.cards) ==2:
                self.blkjck = True

        return self.value


    def get_bust(self):
        '''
        return if hand has bust
        '''
        return self.bust


    def double(self,card):
        '''
        Player doubles hand, hand adds one final card and stays
        '''
        self.bet *= 2
        self.hit(card)
        self.set_stay()


    def split(self):
        '''
        Player splits hand, taking each card and creating a new hand
        Hand must have only two cards that are the same face
        '''
        if self.cards[0].face == self.cards[1].face and len(self.cards) == 2:
            #return a card to be used in a new hand
            return self.cards.pop()


    def splitable(self):
        '''
        Returns True if hand can be split, False otherwise
        '''
        if self.cards[0].face == self.cards[1].face and len(self.cards) == 2:
            return True
        else:
            return False


    def available_actions(self):
        '''
        Returna a string containing a list of the available actions
        '''
        actions = ''
        if self.bust:
            actions = 'Busted!'
        elif self.blkjck:
            actions = 'BlackJack!'
        elif self.stay:
            actions = 'Stay'
        else:
            actions = 'Hit, Stay, Double'
            if self.splitable():
                actions = actions + ', Split'

        return actions


    def finished(self):
        '''
        Returns true if hand is finished (Staying, BlackJack or Busted)
        '''
        if self.stay or self.blkjck or self.bust:
            return True
        else:
            return False


    def final_status(self):
        '''
        Print final status of hand
        '''
        status = str(self)

        if self.blkjck:
            status += ' BlackJack!'
        elif self.bust:
            status += ' Busted!'
        elif self.stay:
            status += ' Staying!'

        print(status)


    def __str__(self):
        '''
        String representation of Hand class
        Concatenate list of cards (suit+face)
        '''
        h = ''
        for i in range(len(self.cards)):
            
            if i > 0:
                h = h + ', '

            h = h + self.cards[i].suit_and_face()

        return h + f' You have {self.value}'
