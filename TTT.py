#TIC-TAC-TOE build 0.0
import random
def get_input (message):
    while True:
        valid_input = input(message)
        if valid_input != "":
            return valid_input
        else:
            print ("Please type in your name, pal :(")
def print_board (board):
    for i in range(9):
        end_char = " | " if (i + 1) % 3 != 0 else "\n"
        print(board[i], end=end_char)
def move():
    while True:
        valid_play = input("Choose a cell to play, from 1 to 9:\n").strip()
        try:
            valid_play = int(valid_play)
        except ValueError:
            print("Please, input a number between 1 and 9.")
            continue
        if 1 <= valid_play <= 9:
            board[valid_play-1] = player_sign
            break
        else:
            print("Please, input a valid cell number between 1 and 9.")
def cpu_move():
    valid_play = random.randint(1, 9)
    if board[valid_play-1] != " ":
        continue
board = [" "] * 9
name = get_input ("Please, tell me your name!\n")
valid_play = 0
print ("Hello ", name, "! Let's get started, shall we?", sep="")
while True:
    player_sign = input("Now, do you want to play as X or 0?\n")
    if player_sign == "x" or player_sign == "X":
        print ("Nice! Let's get going, then!")
        break
    elif player_sign == "o" or player_sign == "O" or player_sign == "0":
        print ("Nice! Let's get going, then!")
        break
    else:
        print ("Please, choose a valid option!")
print_board (board)
move ()
board[valid_play-1] = player_sign
print_board (board)
cpu_move ()
print_board (board)


