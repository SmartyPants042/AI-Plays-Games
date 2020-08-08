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

def random_move(board):
    actions = Board.get_actions(board, True)
    return random.choice(actions)

def print_O_wins():
    print(" ______     ______     __    __     ______        ______     __   __   ______     _____")
    print("/\  ___\   /\  __ \   /\  -./  \   /\  ___\      /\  __ \   /\ \ / /  /\  ___\   /\  == \   ")
    print("\ \ \__ \  \ \  __ \  \ \ \-./\ \  \ \  __\      \ \ \/\ \  \ \ \'/   \ \  __\   \ \  __<   ")
    print(" \ \_____\  \ \_\ \_\  \ \_\ \ \_\  \ \_____\     \ \_____\  \ \__|    \ \_____\  \ \_\ \_\ ")
    print("  \/_____/   \/_/\/_/   \/_/  \/_/   \/_____/      \/_____/   \/_/      \/_____/   \/_/ /_/ ")
    print("                                                                                            ")
    print("                   ______        __     __     __     __   __     ______                    ")
    print("                  /\  __ \      /\ \  _ \ \   /\ \   /\  -.\ \   /\  ___\                   ")
    print("                  \ \ \/\ \     \ \ \/  .\ \  \ \ \  \ \ \-.  \  \ \___  \                  ")
    print("                   \ \_____\     \ \__/ |~\_\  \ \_\  \ \_\\ \_\  \/\_____\                 ")
    print("                    \/_____/      \/_/   \/_/   \/_/   \/_/ \/_/   \/_____/")
    return

def print_X_wins():
    print(" ______     ______     __    __     ______        ______     __   __   ______     _____")
    print("/\  ___\   /\  __ \   /\  -./  \   /\  ___\      /\  __ \   /\ \ / /  /\  ___\   /\  == \   ")
    print("\ \ \__ \  \ \  __ \  \ \ \-./\ \  \ \  __\      \ \ \/\ \  \ \ \'/   \ \  __\   \ \  __<   ")
    print(" \ \_____\  \ \_\ \_\  \ \_\ \ \_\  \ \_____\     \ \_____\  \ \__|    \ \_____\  \ \_\ \_\ ")
    print("  \/_____/   \/_/\/_/   \/_/  \/_/   \/_____/      \/_____/   \/_/      \/_____/   \/_/ /_/ ")
    print("                                                                                            ")
    print("               __  __        __     __     __     __   __     ______                   ") 
    print("              /\_\_\_\      /\ \  _ \ \   /\ \   /\  -.\ \   /\  ___\                  ") 
    print("              \/_/\_\/_     \ \ \/  .\ \  \ \ \  \ \ \-.  \  \ \___  \                 ") 
    print("                /\_\/\_\     \ \__/ .~\_\  \ \_\  \ \_\\ \_\  \/\_____\                ") 
    print("                \/_/\/_/      \/_/   \/_/   \/_/   \/_/ \/_/   \/_____/                ") 
    return

# main game loop
while True:
    Board.print_board(board)
    winner = Board.evaluate(board)
    if winner:
        if winner == 'X':
            print_X_wins()
        else:
            print_O_wins()
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
