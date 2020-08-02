from Board import Board
from AI import move as ai_move
from player import move as player_move

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
        board = ai_move(board)
        print("Got it.")
    # switching the player
    player = not player
