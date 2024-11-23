from random import choice

DUMMY_DECK = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """Returns a random card from the deck"""
    return choice(DUMMY_DECK)

def calculate_score(cards: list):
    """Take a list of cards and return the score calculated from the cards """
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def is_finish(user_score, computer_score):
    if user_score == 0 or computer_score == 0 or user_score > 21:
        return True
    return False

def let_computer_drawing(computer_cards: list):
    computer_score = calculate_score(computer_cards)
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    return calculate_score(computer_cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"
