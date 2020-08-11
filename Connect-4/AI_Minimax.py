from Board import Board
from Minimax import AI

def move(board, player_x=True):
    # assuming the case that human_player == True ONLY.

    action = AI.move(board)
    symbol = 'X' if player_x else 'O'
    board[action[0]][action[1]] = symbol
    return board

################### TESTING ZONE ####################

# board = [
#     ['-', '-', '-', '-',],
#     ['-', '-', '-', 'O',],
#     ['-', 'X', '-', 'O',],
#     ['-', 'X', '-', 'O',],
# ] 
# Board.print_board(move(board))