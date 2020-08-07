from Board import Board
from Minimax import AI

def move(board, human_player=True):
    # assuming the case that human_player == True ONLY.

    action = AI.move(board)
    board[action[0]][action[1]] = 'X'
    return board

################### TESTING ZONE ####################

# board = [
#     ['-', '-', '-', '-',],
#     ['-', '-', '-', 'O',],
#     ['-', 'X', '-', 'O',],
#     ['-', 'X', '-', 'O',],
# ] 
# Board.print_board(move(board))