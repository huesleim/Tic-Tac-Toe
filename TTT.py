    #TIC-TAC-TOE build 0.0
import random
def get_name (message):
    while True:
        valid_input = input(message)
        if valid_input != "":
            return valid_input
        else:
            print ("Please type in your name, pal :(")
            
def assign():
    while True:
        player_sign = input("Now, do you want to play as X or 0?\n")
        if player_sign.lower() == "x":
            print ("Nice! Let's get going, then!")
            cpu_sign = "O"
            return player_sign, cpu_sign
        elif player_sign.lower() == "o" or player_sign == "0":
            print ("Nice! Let's get going, then!")
            cpu_sign = "X"
            return player_sign, cpu_sign
        else:
            print ("Please, choose a valid option!")
            
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
        if board[a] == board[b] == board[c] and board[a] != " ": return True
        else: return False
##            if board[a] == player_sign:
##                print (name, "has won the game!")
##                return player_sign
##            else:
##                print ("I won!")
##                return cpu_sign
##            print ("Want to play again?")

def play_again():
    play_again = input("Want to play again? Type yes or no.\n")
    if play_again.lower() == "yes" or play_again.lower() == "y": return True
    elif play_again.lower() == "no" or play_again.lower() == "n": return False

def show_score():
    print ("Score right now is:\n",name,":", score[0], " x CPU:", score[1], sep="")
    
##def resolve(winner):
##    if winner == player_sign:
##        score[0] += 1
##        print ("You won! Congrats!")
##        show_score()
##        keep_playing = play_again()
##        break
##    elif winner == cpu_sign:
##        score[1] += 1
##        print ("Heh, I won!")
##        show_score()
##        keep_playing = play_again()
##        break
    
name = get_name ("Please, tell me your name!\n")
score = [0,0]
board = [" "] * 9
keep_playing = True
player_sign, cpu_sign = assign()
player_turn = True if player_sign == "x" else False
print ("Hello ", name, "! Let's get started, shall we?", sep="")
print_board (board)

while " " in board and play_again:
    if player_turn:
        player_move ()
        print_board (board)
        player_turn = not player_turn
        if check_win():
            score[0] += 1
            print ("You won! Congrats!")
            show_score()
            keep_playing = play_again()
            board = [" "] * 9
            continue
            
    else:
        print ("My turn now!")
        cpu_move ()
        print_board (board)
        player_turn = not player_turn
        if check_win():
            score[1] += 1
            print ("Heh, I won!")
            show_score()
            keep_playing = play_again()
            board = [" "] * 9
            continue
            


    


# Setting up variables



   


# Win condition


