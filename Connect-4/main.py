from Board import Board
from AI import move as ai_move
from player import move as player_move

import random

# variables init
player = True
board = [
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-'],
]

count = 0

def random_move(board):
    actions = Board.get_actions(board, True)
    return random.choice(actions)

# main game loop
while True:
    Board.print_board(board)
    winner = Board.evaluate(board)
    if winner:
        print(winner, " has won!")
        break

    if player:
        action = player_move(board)
        board[action[0]][action[1]] = 'X'

    else:
        print("Thinking ... ")
        if count < 4:
            action = random_move(board)
            board[action[0]][action[1]] = 'O'
        else:
            board = ai_move(board)
        print("Got it.")
    # switching the player
    player = not player
    count += 1
    