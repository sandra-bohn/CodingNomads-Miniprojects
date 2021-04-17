"""
# Rock-Paper-Scissors Game

Code a game of rock paper scissors.

## Instructions

* take in a number 0-2 from the user that represents their hand
* generate a random number 0-2 to use for the computer's hand
* call the function `get_hand` to get the string representation of the user's hand
* call the function `get_hand` to get the string representation of the computer's hand
* call the function `determine_winner` to figure out who won
* print out the player hand and computer hand
* print out the winner

## Some Tips

Creating a function that gets a "hand" based on a number.

The function should take in a number and return the string representation of the hand. E.g.:
"""
import random
def get_hand(hand: int):
    # 0 = scissor, 1 = rock, 2 = paper
    hands = {0: 'scissor', 1: 'rock', 2: 'paper'}
    # for example if the variable hand is 0, it should return the string "scissor"
    output = hands[hand]
    return output

def determine_winner(hand1: str, hand2: str):
    output = ''
    if hand1 == 'scissor' and hand2 == 'scissor':
        output = 'You tied!'
    if hand1 == 'scissor' and hand2 == 'rock':
        output = 'Computer wins!'
    if hand1 == 'scissor' and hand2 == 'paper':
        output = 'You win!'

    if hand1 == 'rock' and hand2 == 'rock':
        output = 'You tied!'
    if hand1 == 'rock' and hand2 == 'paper':
        output = 'Computer wins!'
    if hand1 == 'rock' and hand2 == 'scissor':
        output = 'You win!'

    if hand1 == 'paper' and hand2 == 'paper':
        output = 'You tied!'
    if hand1 == 'paper' and hand2 == 'scissor':
        output = 'Computer wins!'
    if hand1 == 'paper' and hand2 == 'rock':
        output = 'You win!'
    return output

# Get user's hand
user_num = int(input('Enter a number between 0 and 2 (0 = scissor, 1 = rock, 2 = paper): '))
# Generate computer's hand
comp_num = int(random.randrange(0, 3, 1))
# Get hands from numbers
user_hand = get_hand(user_num)
comp_hand = get_hand(comp_num)
# Determine winner
who_won = determine_winner(user_hand, comp_hand)
# Print player hand, computer hand, and winner
print(f'You chose {user_hand} and computer chose {comp_hand}. {who_won}')
