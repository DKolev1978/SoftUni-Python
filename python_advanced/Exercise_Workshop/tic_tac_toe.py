# import speech_recognition as sr

from collections import deque
# from pyfiglet import Figlet


def check_for_win():
    player_name, player_symbol = players[0]

    first_diagonal_win = all([board[i][i] == player_symbol for i in range(SIZE)])  # Winning logic primary diagonal
    second_diagonal_size = all(
        [board[i][SIZE - i - 1] == player_symbol for i in range(SIZE)])  # Winning logic secondary diagonal
    row_win = any(all(player_symbol == pos for pos in row) for row in board)  # Winning logic row diagonal
    col_win = any(
        [all(board[r][c] == player_symbol for r in range(SIZE)) for c in range(SIZE)])  # Winning logic column diagonal

    if any([first_diagonal_win, second_diagonal_size, row_win, col_win]):
        print_board()
        print(f"{player_name} WON!")

        raise SystemExit


def place_symbol(row, col):
    board[row][col] = players[0][1]

    check_for_win()
    print_board()

    if turns == SIZE * SIZE:
        print("Draw!")
        raise SystemExit

    players.rotate()


def chose_position():
    global turns

    while True:
        try:
            position = int(input(f"{players[0][0]} choose a free position in range [1-{SIZE * SIZE}]: "))
            row, col = (position - 1) // SIZE, (position - 1) % SIZE
        except ValueError:
            print(f"{players[0][0]}, please select a valid position")
            continue

        if 1 <= position <= SIZE * SIZE and board[row][col] == ' ':
            turns += 1
            place_symbol(row, col)
        else:
            print(f"{players[0][0]}, please select a valid position")


def start():
    # figlet = Figlet(font="big")
    # print(figlet.renderText("Tic-Tac-Toe"))

    player_one_name = input("Player one, please enter your name: ")
    player_two_name = input("Player two, please enter your name: ")
    while True:
        player_one_symbol = input(f"{player_one_name}, please chose 'X' or 'O'?").upper()
        if player_one_symbol not in ["X", "O"]:
            print(f"{player_one_name}, please select a valid symbol 'X' or 'O'!")
        else:
            break

    player_two_symbol = "O" if player_one_symbol == "X" else "X"

    players.append([player_one_name, player_one_symbol])
    players.append([player_two_name, player_two_symbol])

    print_board(begin=True)
    chose_position()


def print_board(begin=False):
    if begin:
        print("This is the numeration of the board:")
        [print(f"| {' | '.join(row)} |") for row in board]

        for row in range(SIZE):
            for col in range(SIZE):
                board[row][col] = ' '
    else:
        [print(f"| {' | '.join(row)} |") for row in board]


SIZE = 3
turns = 0

board = [[str(i), str(i + 1), str(i + 2)] for i in range(1, SIZE * SIZE + 1, SIZE)]
players = deque()

start()
