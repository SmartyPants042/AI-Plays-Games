from ProductionBuild import MCTS
from Board import Board

def move(board):
    return MCTS.main(board, verbose=True)
    
################### TESTING ZONE ####################

# board = [
#     ['-', '-', '-', '-',],
#     ['-', 'X', '-', '-',],
#     ['-', 'X', '-', 'O',],
#     ['-', 'X', '-', 'O',],
# ] 
# Board.print_board(move(board))