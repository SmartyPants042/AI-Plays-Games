from Board import Board
from AI_MCTS import move as mcts_move
from AI_Minimax import move as minimax_move

import random
import time

# variables init
player = True
board = [
    ['-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-'],
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
        print("X's Turn: Thinking ... ")
        start = time.process_time()
        board = minimax_move(board, human_player=True)
        print(f"Got it. Took {round(time.process_time()-start, 2)} seconds")
    else:
        print("O's Turn: Thinking ... ")
        start = time.process_time()
        board = mcts_move(board, human_player=False)
        print(f"Got it. Took {round(time.process_time()-start, 2)} seconds")
    
    # switching the player
    player = not player
    count += 1