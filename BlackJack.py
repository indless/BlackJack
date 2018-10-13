'''
Play a game of BlackJack!
'''
#from BlackJack.Player import Player
from Player import Player
from Deck import Deck
from Hand import Hand


def setup_game():
    '''
    Initialize BlackJack game
    '''
    global blackjackplayers

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
        #add Player to list of players
        blackjackplayers.append(Player(playerid=p))
        #set name of each Player
        blackjackplayers[p].set_name()


def play_a_round():
    '''
    Deal a round of BlackJack to each player
    '''
    global blackjackhands
    global blackjackplayers

    # get each player's bets
    get_all_player_bets()
    
    # create hand for each player
    blackjackhands = []
    for p in blackjackplayers:
        blackjackhands.append(Hand(playerid = p.id,bet=p.bet))

    # deal round
    deal()


def get_all_player_bets():
    '''
    Get each player's bet
    '''
    global blackjackplayers

    for p in blackjackplayers:
        #if player is broke, ask if they would like to buy back in
        if p.get_bankroll() == 0:
            if 'n' != input(f'{p.name}, you are broke! Would you like to buy back in? y/n ').lower():
                p.set_bankroll()
        
        #if player has money, create a hand. ignore players that are broke!
        if p.get_bankroll() > 0:
            p.ask_for_bet()
        else:
            #remove broke players
            blackjackplayers.pop(blackjackplayers.index(p))


def deal():
    '''
    Deal round to each player
    '''
    global blackjackhands
    global blackjackplayers
    global dealerhand
    global dealer
    nodealerblackjack = True
    dealerhand = Hand()
    #deal first two cards to each hand
    for _ in range(2):
        
        for h in blackjackhands:
            #print player name, take a card and show hand
            print(blackjackplayers[h.playerid].name)
            h.hit(gamedeck.nextcard())
            print(h)

        #deal card to dealer hand last
        print(dealer.name)
        dealerhand.hit(gamedeck.nextcard())
        #need to hide dealers first card so they don't know
        if len(dealerhand.cards) == 1:
            print(f'{dealer.name} showing hidden card')
        elif len(dealerhand.cards) == 2:
            print(f'{dealer.name} showing {dealerhand.cards[1].suit_and_face()}')
        
    #check for Dealer BlackJack
    if dealerhand.get_value() == 21:
        #check other hands for blackjack, pay them
        for h in blackjackhands:
            #check for player blackjacks
            if h.blkjck:
                theplayer = blackjackplayers[h.playerid]
                #pay blackjack
                theplayer.win(2.5*h.bet)
                #notify player of blackjack
                print(f'{theplayer.name}, your hand is {h}. BlackJack!\n You win: {2.5*h.bet}!')
                #remove hand
                blackjackhands.pop(blackjackhands.index(h))

        #notify all players of dealer blackjack
        print(f'Dealer BlackJack! {dealerhand}')
        print('Everyone loses this round except BlackJacks!')
        nodealerblackjack = False
    
    if nodealerblackjack:
        # need a counter to be used in the event of a split hand to insert after current index so the same player can continue with their new hand after finishing the current one
        x = 0
        # for each hand **will it create an issue if I add another hand to the list after current hand?
        for h in blackjackhands:
            x+=1
            
            while True:
                #check for blackjack: would only happen on split hands
                if h.blkjck:
                    theplayer = blackjackplayers[h.playerid]
                    #pay blackjack
                    theplayer.win(2.5*h.bet)
                    #notify player of blackjack
                    print(f'{theplayer.name}, your hand is {h}. BlackJack!\n You win: {2.5*h.bet}!')
                    #remove hand
                    blackjackhands.pop(blackjackhands.index(h))
                    break
                
                action = ''
                
                #print player name, hand cards and value
                print(f'{blackjackplayers[h.playerid].name}, your hand is: {h}')
                
                #use player ID to ask player what they want to do based on the actions available from the hand
                action = blackjackplayers[h.playerid].ask_for_action(h.available_actions())

                #execute action
                if action == 'stay':
                    h.stay = True
                elif action == 'hit':
                    h.hit(gamedeck.nextcard())
                elif action == 'double':
                    h.double(gamedeck.nextcard())
                elif action == 'split':
                    #create a split hand with same player ID as current hand
                    newhandfromsplit = Hand(h.playerid,h.bet)
                    #insert one of the cards from current hand into the split hand
                    newhandfromsplit.hit(h.split())
                    #insert the split hand after the current hand to allow the same player to play it after current hand
                    blackjackhands.insert(x,newhandfromsplit)
                    #hit this hand to give it a second card
                    h.hit(gamedeck.nextcard())
                    #hit the split hand to give it a second card
                    blackjackhands[x].hit(gamedeck.nextcard())
                
                #stay, blkjack or bust
                if h.finished():
                    h.final_status()
                    break

        #dealer's turn
        while not dealerhand.finished() or dealerhand.get_value() < 16 or dealerhand.soft16:
            
            #show dealers hidden card if this is start of dealer's turn
            if len(dealerhand.cards) == 2:
                #print dealer name to show it's dealer's turn
                print(dealer.name)
                print(dealerhand)
            
            if dealerhand.get_value() < 16 or dealerhand.soft16:
                #print dealer name to show it's dealer's turn
                print(dealer.name)
                dealerhand.hit(gamedeck.nextcard())
                print(dealerhand)
            else:
                dealerhand.set_stay()
        
        #determine winners and pay them
        #announce dealer hand
        print(dealer.name)
        dealerhand.final_status()
        #announce each players hand, win/lose
        for h in blackjackhands:
            #determine if player wins, pushes or loses
            if (h.get_value() > dealerhand.get_value() and not h.bust and not dealerhand.bust) or dealerhand.bust and not h.bust:
                #player receives bet & winnings of bet or bet*2)
                blackjackplayers[h.playerid].win(h.bet*2)
                print(f'{blackjackplayers[h.playerid].name}, you win: {h.bet*2}!')
            elif h.get_value() == dealerhand.get_value() and not h.bust:
                #return bet on push
                blackjackplayers[h.playerid].win(h.bet)
                print(f'{blackjackplayers[h.playerid].name}, you push, bet returned!')
            else:
                print(f'{blackjackplayers[h.playerid].name}, you lost your bet: {h.bet}!')
        #don't pay blackjack hands if they've already been paid
        #need to automate the play of the dealer's hand to hit on 15 and soft 16

# Play BlackJack

# Play BlackJack until players all stop
while True:
    #list of dealer and all players
    print('Now playing BlackJack!')
    blackjackplayers = []
    blackjackhands = []
    dealer = Player(name='Dealer')
    dealerhand = Hand()
    gamedeck = Deck()
    
    setup_game()
    
    while True:
        play_a_round()

        if 'n' == input('Play another round? (y/n) ').lower():
            # print each players name and bankroll
            for p in blackjackplayers:
                print(p)
            break

    if 'n' == input('Start a new game? (y/n) ').lower():
        print('Thanks for playing BlackJack!')
        break
