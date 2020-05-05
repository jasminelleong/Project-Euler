# In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:
#
# High Card: Highest value card.
# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
# Straight: All cards are consecutive values.
# Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of same suit.
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
#
# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
#
# If two players have the same ranked hands then the rank made up of the highest value wins; for example,
# a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have
# a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then
# the next highest cards are compared, and so on.
#
# Consider the following five hands dealt to two players:
# Hand	 	Player 1	 	Player 2	 	Winner
# 1	 	5H 5C 6S 7S KD
# Pair of Fives
# 2C 3S 8S 8D TD
# Pair of Eights
# Player 2
# 2	 	5D 8C 9S JS AC
# Highest card Ace
# 2C 5C 7D 8S QH
# Highest card Queen
# Player 1
# 3	 	2D 9C AS AH AC
# Three Aces
# 3D 6D 7D TD QD
# Flush with Diamonds
#     Player 2
# 4	 	4D 6S 9H QH QC
# Pair of Queens
# Highest card Nine
# 3D 6D 7H QD QS
# Pair of Queens
# Highest card Seven
# Player 1
# 5	 	2H 2D 4C 4D 4S
# Full House
# With Three Fours
# 3C 3D 3S 9S 9D
# Full House
# with Three Threes
# Player 1
#
# The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten
# cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards.
# You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no
# specific order, and in each hand there is a clear winner.
#
# How many hands does Player 1 win?
from typing import List

hands_data = open('054_poker.txt', 'r').read()
game_rounds = [line for line in hands_data.split('\n') if line != '']
rounds_cards = [card for card in [game_round.split(' ') for game_round in game_rounds]]

rounds_manifest = []
p1_wins = 0


def calculate_score(hand: List[dict]) -> int:
    value_map = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
    }

    hand_values = sorted([value_map[card['value']] for card in hand])
    hand_suits = [card['suit'] for card in hand]
    values_counts = {}
    for value in hand_values:
        if value in values_counts:
            values_counts[value] += 1
        else:
            values_counts[value] = 1

    # Quick analysis shows there's no straight flushes in the input file, so we won't check.

    # Check for four of a kind
    if 4 in values_counts.values():
        return 100000 + hand_values[-1]

    # Check for full house
    if 3 in values_counts.values() and 2 in values_counts.values():
        return 50000 + hand_values[-1]

    # Check for flush
    is_flush = len(set(hand_suits)) == 1
    if is_flush:
        return 10000 + hand_values[-1]

    # Check for straight
    is_straight = all([value in hand_values for value in range(hand_values[0], hand_values[0] + 5)])
    if is_straight:
        return 5000 + hand_values[-1]

    # Check for three of a kind
    if 3 in values_counts.values():
        return 1000 + hand_values[-1]

    # Check for two pair
    if 2 in values_counts.values():
        pairs = [key for key in values_counts.keys() if values_counts[key] == 2]
        if len(pairs) == 2:
            return 500 + hand_values[-1]

    # Check for one pair
    if 2 in values_counts.values():
        return 10 * [card_value for card_value in values_counts.keys() if values_counts[card_value] == 2][0] \
               + hand_values[-1]

    # You got plenty of nuttin'
    return hand_values[-1]


for round_cards in rounds_cards:
    cards = [
        {
            'value': card[0],
            'suit': card[1]
        }
        for card in round_cards
    ]

    p1_hand = cards[:5]
    p2_hand = cards[5:]

    round_info = {
        'p1_hand': p1_hand,
        'p2_hand': p2_hand
    }

    p1_score = calculate_score(p1_hand)
    p2_score = calculate_score(p2_hand)

    if p1_score == p2_score:
        print('TIE:')
        print(p1_hand)
        print(p2_hand)

    if p1_score > p2_score:
        p1_wins += 1

print(p1_wins)
