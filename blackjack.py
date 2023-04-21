import random

# create deck of cards and the dealer and players hand
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
        'Jack', 'Queen', 'King', 'Ace', 'Jack', 'Queen', 'King', 'Ace', 
        'Jack', 'Queen', 'King', 'Ace', 'Jack', 'Queen', 'King', 'Ace']
player_hand = []
dealer_hand = []
player_in = True
dealer_in = True

# deal out the cards
def deal_cards(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.pop(card)

# calculate the total of each hand
def calculate_total(hand):
    total = 0
    face = ['Jack', 'Queen', 'King']
    for card in hand:
        if card in range(1, 11):
            total += card
        elif card in face:
            total += 10
        else:
            if total > 11:
                total += 1
            else:
                total += 11
    return total


# check for winner
def reveal_dealer_hand():
    if len(dealer_hand) == 2:
        return dealer_hand[0]
    elif len(dealer_hand) > 2:
        return dealer_hand[0], dealer_hand[1]
    

# continue to play game
for _ in range(2):
    deal_cards(dealer_hand)
    deal_cards(player_hand)

while player_in or dealer_in:
    print('Dealer has {reveal_dealer_hand()} and X')
    print('You have {player_hand} for a total of {calculate_total(player_hand)}')
    if player_in:
        stay_or_hit = input('1: Stay\n2: Hit\n')
    if calculate_total(dealer_hand) > 16:
        dealer_in = False
    else:
        deal_cards(dealer_hand)
    if stay_or_hit == '1':
        player_in = False
    else:
        deal_cards(player_hand)
    if calculate_total(player_hand) >= 21:
        break
    elif calculate_total(dealer_hand) >= 21:
        break

if calculate_total(player_hand) == 21:
    print('\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has a {dealer_hand} for a total of {calculate_total(dealer_hand)}')
print(player_hand)
print(dealer_hand)