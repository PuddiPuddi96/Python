from art import logo, vs
from game_data import get_random_account, get_element_info, get_follower_count, check_accounts
from utils import check_answer, get_user_guess


game_over = False
final_score = 0

account_a = get_random_account()
account_b = get_random_account()

check_accounts(account_a, account_b)

while not game_over:
    print(logo)

    if final_score != 0:
        print(f"You're right! Current score: {final_score}")

    print(f"Compare A: {get_element_info(account_a)}")
    print(vs)
    print(f"Against B: {get_element_info(account_b)}")

    guess = get_user_guess()
    if check_answer(guess, get_follower_count(account_a), get_follower_count(account_b)):
        final_score += 1
        if get_follower_count(account_a) < get_follower_count(account_b):
            account_a = account_b

        account_b = get_random_account()
        check_accounts(account_a, account_b)
    else:
        game_over = True

    print("\n" * 20)

print(logo)
print(f"Sorry, that's wrong. Final score: {final_score}")
