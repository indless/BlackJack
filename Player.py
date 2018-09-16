'''
A player at the blackjack table
'''

class Player():

    def __init__(self,playerid=0,name='Player Name',bankroll=100,busted=False,playing=True):

        self.id = playerid
        self.name = name
        self.bankroll = bankroll
        self.busted = busted
        self.playing = playing


    def get_id(self):
        '''
        Returns the ID of the player
        '''
        return self.id


    def set_name(self):
        '''
        Prompts user to input player name
        '''
        self.name = input('Please enter your name: ')


    def get_bankroll(self):
        '''
        Returns the current value of the player's bankroll
        '''
        return self.bankroll


    def set_bankroll(self,bankroll=100):
        '''
        Sets new bankroll for player
        '''
        self.bankroll = bankroll


    def ask_for_bet(self):
        '''
        Prompts user to input bet amount
        '''
        while True:
            try:
                betthis = int(input(f'{self.name}, your current Bankroll is {self.bankroll}\nHow much would you like to bet? '))
            except:
                print("Whoops! That is not a number")
            else:
                #make sure player has sufficient bankroll to cover the bet
                if betthis <= self.bankroll:
                    self.set_bet(betthis)
                    break


    def set_bet(self,bet=10):
        '''
        Player bets, if player bankroll can cover the bet, bet value is set and bankroll is reduced by bet amount
        '''
        if self.bankroll >= bet:
            self.bet = bet
            self.bankroll -= bet


    def double_or_split(self):
        '''
        Player doubles or splits hand, placing an additional bet of the same value and reducing player bankroll accordingly
        '''
        #how will this handle insufficient bankroll????
        self.bet(self.bet)
        return self.bet


    def win(self,amount=10):
        '''
        The players hand wins, bankroll is increased by the amount of the winnings
        '''
        self.bankroll += amount


    def __str__(self): #player_details(self):
        '''
        Creates a readable form of a player object when printed
        '''
        print(f'Player Name: {self.name}')
        print(f'Bankroll: {self.bankroll}')
        print(f'Busted: {self.busted}')
        print(f'Playing: {self.playing}')
