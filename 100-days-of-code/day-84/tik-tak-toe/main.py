def check_win(board):
    lines = []
    lines.extend(board)  # horizontal lines
    lines.extend(zip(*board))  # vertical lines
    lines.append([board[i][i] for i in range(3)])  # main diagonal
    lines.append([board[i][2 - i] for i in range(3)])  # secondary diagonal

    for line in lines:
        if line.count(line[0]) == 3 and line[0] != " ":
            return True
    return False

def check_tie(board):
    for row in board:
        if " " in row:
            return False
    return True

def move(board, player):
     while True:
        try:
            print(f"It's player {player} turn!")
            row = int(input('Enter row (from 1 to 3): '))
            col = int(input('Enter column (from 1 to 3): '))
            if(row >= 1
               and row <= 3
               and col >= 1
               and col <= 3
               and board[row - 1][col - 1] == " "
            ):
                board[row - 1][col - 1] = player
                break
            else:
                print("Invalid move. Please try again.")
        except IndexError:
            print("Invalid input. Row and column must be between 1 and 3.")

def print_grid(board):
    for row in board:
        print("|" + "|".join(row) + "|")

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_grid(board)
        move(board, current_player)

        if check_win(board):
            print_grid(board)
            print(f"Player {current_player} wins!")
            break
        if check_tie(board):
            print_grid(board)
            print("The game is a tie!")
            break
        
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"
    
    print("Game over!")

def main():
    play_game()

if __name__ == '__main__':
    main()
