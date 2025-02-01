def check():
    pass

def print_grid():
    pass

def play_game():
    pass

def close_game():
    pass


def main():
    correct_input = False

    while not correct_input:
        answer = input('').upper()
        if answer == 'Y':
            correct_input = True
            play_game()
        elif answer == 'N':
            correct_input = True
            close_game()
        else:
            print('')

if __name__ == '__main__':
    main()
