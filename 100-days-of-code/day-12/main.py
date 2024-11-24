from art import logo
from utils import check_answer, set_difficulty, get_number_to_guess


print(logo)

print("Welcome to the  Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number_to_guess = get_number_to_guess()
number_attempts = set_difficulty()

while number_attempts > 0 and number_attempts != -1:
    print(f"You have {number_attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    number_attempts = check_answer(guess, number_to_guess, number_attempts)

if number_attempts == 0:
    print("You've run out of guesses, you lose.")
    print(f"The number was {number_to_guess}")
elif number_attempts == -1:
    print("Congratulations, you won!")
