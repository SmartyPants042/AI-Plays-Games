from Board import Board
from AI_Minimax import move as minimax_move 
from player import move as player_move

import random
import time

def random_move(board, player_x, level):
    actions = Board.get_actions(board, player_x)
    action = random.choice(actions)

    if player_x:
        board[action[0]][action[1]] = 'X'
    else:
        board[action[0]][action[1]] = 'O'

    return board

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

def print_start():
    print(" _____ _        _               _                ")
    print("|_   _(_)      | |             | |               ")
    print("  | |  _  ___  | |_ __ _  ___  | |_ ___   ___     ")
    print("  | | | |/ __| | __/ _` |/ __| | __/ _ \ / _ \   ")
    print("  | | | | (__  | || (_| | (__  | || (_) |  __/   ")
    print("  \_/ |_|\___|  \__\__,_|\___|  \__\___/ \___|   ")
    
    return

def get_player(char):
    char = char[0]

    if char == '1':
        return player_move
    elif char == '2':
        return minimax_move
    elif char == '3':
        return random_move
    
    return None 
    
def print_menu():

    print("Menu: ")
    print("1. You")
    print("2. Minimax")
    print("3. Random")

    player1 = None
    while player1 == None:
        player1 = get_player(input("Enter Player1: "))
    
    level1 = 0
    if player1 == minimax_move:
        level1 = float(input("Input level for minimax (1-5 depth): "))

    player2 = None
    while player2 == None:
        player2 = get_player(input("Enter Player2: "))
    
    level2 = 0
    if player2 == minimax_move:
        level2 = float(input("Input level for minimax (1-5 depth): "))

    return player1, level1, player2, level2

def game_play(player1, level1, player2, level2):
    # variables init
    player = True
    board = Board.get_initial_state()

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
            try:
                board = player1(board, player_x=True, level=level1)
            except:
                break
            print(f"Got it. Took {round(time.process_time()-start, 2)} seconds")
        else:
            print("O's Turn: Thinking ... ")
            start = time.process_time()
            try:
                board = player2(board, player_x=False, level=level2)
            except:
                break

            print(f"Got it. Took {round(time.process_time()-start, 2)} seconds")
        
        # switching the player
        player = not player
    
    print("DONE")

if __name__ == "__main__":
    print_start()
    while True:
        player1, level1, player2, level2 = print_menu()        
        game_play(player1, level1, player2, level2)

        repeat = input("continue? (y/else): ")
        if repeat == 'y' or repeat == "yes":
            pass
        else:
            print("Byee")
            break
            
