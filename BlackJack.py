'''
Play a game of BlackJack!
'''
from BlackJack.Player import Player
from BlackJack.Deck import Deck
# Play BlackJack

# Play BlackJack until players all stop
while True:
    #list of dealer and all players
    print('Now playing BlackJack!')
    blackjackplayers = []
    gamedeck = Deck()
    
    initialize()
    
    while True:
        play_a_round()

        if 'n' == input('Play another round? (y/n) '.lower()):
            break

    if 'n' == input('Start a new game? (y/n) '.lower()):
        print('Thanks for playing BlackJack!')
        break


def initialize():
    #initialize Dealer
    dealer = Player(name='Dealer')
    blackjackplayers.append(dealer)

    #will need to add starting bankroll prompt if you would like to change it

    #get number of players
    while True:
            try:
                playercount = int(input(f'How many players are there? '))
            except:
                print("Whoops! That is not a number")
            else:
                #make sure there's a player
                if playercount >= 0:
                    break

    for p in range(playercount):
        blackjackplayers.append(Player(playerid=p))
        blackjackplayers[p].set_name()


def play_a_round():
    get_all_player_bets()


def get_all_player_bets():
    #get each player's bet
    for p in range(1,len(blackjackplayers)):
        blackjackplayers[p].ask_for_bet()
    