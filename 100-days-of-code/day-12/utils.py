from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user_guess, answer, turns):
    if user_guess > answer:
        print("Too high.")
        return turns - 1
    elif user_guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")
        return - 1

def set_difficulty():
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if difficulty == "easy":
            return EASY_LEVEL_TURNS
        elif difficulty == "hard":
            return HARD_LEVEL_TURNS
        else:
            print("Invalid input. Please choose 'easy' or 'hard'.")

def get_number_to_guess():
    return randint(1, 100)
