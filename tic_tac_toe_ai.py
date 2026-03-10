# ======================================================
# TIC TAC TOE AI
# Minimax Algorithm Implementation
# ======================================================

import math

# board representation
board = [" " for _ in range(9)]

HUMAN = "X"
AI = "O"


# ------------------------------------------------------
# Display Board
# ------------------------------------------------------

def print_board():
    print()
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
    print()


# ------------------------------------------------------
# Check Winner
# ------------------------------------------------------

def check_winner(player):

    win_patterns = [
        [0,1,2],[3,4,5],[6,7,8],  # rows
        [0,3,6],[1,4,7],[2,5,8],  # columns
        [0,4,8],[2,4,6]           # diagonals
    ]

    for pattern in win_patterns:
        if all(board[i] == player for i in pattern):
            return True

    return False


# ------------------------------------------------------
# Check Draw
# ------------------------------------------------------

def is_draw():
    return " " not in board


# ------------------------------------------------------
# Minimax Algorithm
# ------------------------------------------------------

def minimax(depth, is_maximizing):

    if check_winner(AI):
        return 1

    if check_winner(HUMAN):
        return -1

    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = AI
                score = minimax(depth+1, False)
                board[i] = " "
                best_score = max(score, best_score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = HUMAN
                score = minimax(depth+1, True)
                board[i] = " "
                best_score = min(score, best_score)

        return best_score


# ------------------------------------------------------
# AI Move
# ------------------------------------------------------

def ai_move():

    best_score = -math.inf
    move = None

    for i in range(9):
        if board[i] == " ":

            board[i] = AI
            score = minimax(0, False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    board[move] = AI


# ------------------------------------------------------
# Human Move
# ------------------------------------------------------

def human_move():

    while True:
        try:
            pos = int(input("Enter position (1-9): ")) - 1

            if board[pos] == " ":
                board[pos] = HUMAN
                break
            else:
                print("Position already taken!")

        except:
            print("Invalid input!")


# ------------------------------------------------------
# Game Loop
# ------------------------------------------------------

print("Tic Tac Toe AI")
print("You are X, AI is O")
print_board()

while True:

    human_move()
    print_board()

    if check_winner(HUMAN):
        print("You win!")
        break

    if is_draw():
        print("Game Draw!")
        break

    ai_move()
    print("AI move:")
    print_board()

    if check_winner(AI):
        print("AI wins!")
        break

    if is_draw():
        print("Game Draw!")
        break