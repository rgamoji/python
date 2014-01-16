#!/usr/bin/env python
"""
Small tic-tac-toe kind of game. 
You get 4 turns to guess the row and column in the matrix (ocean) to guess where the battle ship is hidden. 
Ex:
$ ./battle_ship_game.py 
Let's play Battleship!
O O O O O
O O O O O
O O O O O
O O O O O
O O O O O
Guess Row:2
Guess Col:2
You missed my battleship!
Guess Row:1
Guess Col:0
You missed my battleship!
Guess Row:4
Guess Col:3
You missed my battleship!
Guess Row:2
Guess Col:1
You missed my battleship!
Game Over
O S O O O
X O O O O
O X X O O
O O O O O
O O O X O
"""
from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
board[ship_row][ship_col]="S"

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!

for turn in range(4):
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
	print_board(board)
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        if turn == 3:
            print "Game Over"
	    print_board(board)
    # Print (turn + 1) here!

