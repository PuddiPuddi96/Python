def get_user_guess():
    insert_input = False
    user_guess = ""

    while not insert_input:
        user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        if user_guess not in "ab":
            print("Invalid input. Try again.")
        else:
            insert_input = True

    return user_guess


def check_answer(user_guess, account_a_followers, account_b_followers):
    if account_a_followers > account_b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"
