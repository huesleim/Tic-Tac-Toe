#TIC-TAC-TOE build 0.0
import random
def get_name (message):
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
def player_move():
    while True:
        valid_play = input("Choose a cell to play, from 1 to 9:\n").strip()
        try:
            valid_play = int(valid_play)
        except ValueError:
            print("Please, input a number between 1 and 9.")
            continue
        if 1 <= valid_play <= 9 and board[valid_play-1] == " ":
            board[valid_play-1] = player_sign
            break
        else:
            print("Please, input a valid, empty cell number between 1 and 9.")
def cpu_move():
    valid_play = random.randint(1, 9)
    if board[valid_play-1] != " ":
        cpu_move()
    else: board[valid_play-1] = cpu_sign

def check_win():
    winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for combo in winning_combinations:
        a, b, c = combo
        if board[a] == board[b] == board[c] and board[a] != " ":
            if board[a] == player_sign:
                print (name, "has won the game!")
                return player_sign
            else:
                print ("I won!")
                return cpu_sign
            print ("Want to play again?")

# Setting up variables
winner = 0  
valid_play = 0
board = [" "] * 9
name = get_name ("Please, tell me your name!\n")
print ("Hello ", name, "! Let's get started, shall we?", sep="")
switch = True

# Setting up each player's sign

while True:
    player_sign = input("Now, do you want to play as X or 0?\n")
    if player_sign.lower() == "x":
        print ("Nice! Let's get going, then!")
        break
    elif player_sign.lower() == "o" or player_sign == "0":
        print ("Nice! Let's get going, then!")
        break
    else:
        print ("Please, choose a valid option!")
if player_sign == "x" or player_sign == "X": cpu_sign = "O"
else: cpu_sign = "X"

# Game

print_board (board)
while " " in board and not winner:
    if switch:
        player_move ()
        print_board (board)
        switch = not switch
    else:
        print ("My turn now!")
        cpu_move ()
        print_board (board)
        switch = not switch
    winner = check_win()
    if winner: break
   
 
    winner = check_win()
    if winner: break

# Win condition


