# Blackjack CLI game
from numpy import random

player_wins = []
cards_in_play = []

# Build deck    
number_of_decks = 10
suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
cards_in_suit = [2,3,4,5,6,7,8,9,10,'Jack', 'Queen', 'King', 'Ace']
deck = []

for batch in range(number_of_decks):
    for suit in suits:
        for card in cards_in_suit:
            deck.append(f'{card} of {suit}')

live_deck = deck.copy() 

def deal_cards(game_deck):
        card = random.choice(game_deck)
        game_deck.pop(game_deck.index(card))
        return card

def score(hand):
    score = 0
    aces = 0
    for card in hand:
        val_suit = card.split(' of ')
        val = val_suit[0]
        
        if val == 'Ace':
            aces += 1
            val = 11
        elif val in ['Jack', 'Queen', 'King']:
            val = 10
        
        score += int(val)
        
    if score > 21:
        score = score - 10 * aces
    return score

def hit_stick_dealer(hand, min_score = 17):
        if score(hand) >= min_score:
            return hand.copy()
            
        else:
            card = random.choice(live_deck)
            hand.append(card)
            live_deck.pop(live_deck.index(card))
            return hit_stick_dealer(hand)   

def hit_stick(player_hand, dealer_hand):
        hit = input('Hit or stick? ')

        if hit == 'stick':
            dealer_hand = hit_stick_dealer(dealer_hand)
            dealer_score = score(dealer_hand)
            print('Dealer:', dealer_hand, dealer_score)
            return dealer_hand.copy()

        elif hit == 'hit':
            player_card = random.choice(live_deck)
            player_hand.append(player_card)
            live_deck.pop(live_deck.index(player_card))

            if score(player_hand) > 21:
                print('Player Bust', player_hand, score(player_hand))
                
                dealer_hand = hit_stick_dealer(dealer_hand)
                dealer_score = score(dealer_hand)
                
                print('Dealer:', dealer_hand, dealer_score)
                return dealer_hand.copy()
            else:
                print('Player:', player_hand, score(player_hand))
                hit_stick(player_hand, dealer_hand)
        else:
            hit_stick(player_hand, dealer_hand)

def blackjack(ret_count = False):
    print('\n-------- New Game -------\n')
    player_win = 0

    player_card_1 = deal_cards(live_deck)
    dealer_card_1 = deal_cards(live_deck)
    player_card_2 = deal_cards(live_deck)
    dealer_card_2 = deal_cards(live_deck)

    player_hand = list([player_card_1, player_card_2])
    dealer_hand = list([dealer_card_1, dealer_card_2])

    player_score = score(player_hand)
    dealer_score = score(dealer_hand)

    if player_score == 21:
        player_win += 1
        print('Blackjack: ', player_hand, player_score)
        print('Dealer: ', dealer_hand, dealer_score)
        print('Player Wins', end = '\n')


    elif dealer_score == 21:
        print('Player: ', player_hand, player_score)
        print('Blackjack: ', dealer_hand, dealer_score)
        print('House Wins')

    else:
        print('Player: ', player_hand, player_score)    
        hit_stick(player_hand, dealer_hand)
        player_score = score(player_hand)
        dealer_score = score(dealer_hand)

        if player_score <= 21 and (player_score > dealer_score or dealer_score > 21):
            player_win += 1
            print('Player Wins', end = '\n')

        elif player_score == dealer_score:
            player_win += 1
            print('Push : no winner', end = '\n')

        else:
            print('Dealer Score:', dealer_score)
            print('House Wins', end = '\n')

    if ret_count == True:
        return player_win

if __name__ == "__main__":
    print(
        '''
        #######################################################################################
        #######################################################################################
        ###################################### BLACKJACK ######################################
        #######################################################################################
        #######################################################################################
        ''')
    runs = input('How many games? ')
    for i in range(int(runs)):
        player_wins.append(blackjack(ret_count=True))

    print('################################')    
    print('-------- Player Win Rate -------')
    print(
        round(100 * sum(player_wins) / len(player_wins))
        , '%')
    print('################################')