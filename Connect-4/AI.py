from ProductionBuild import MCTS
from Board import Board

def move(board, human_player=False):
    return MCTS.main(board, verbose='v', human_player=human_player)
    
################### TESTING ZONE ####################

# board = [
#     ['-', '-', '-', '-',],
#     ['-', 'X', '-', '-',],
#     ['-', 'X', '-', 'O',],
#     ['-', 'X', '-', 'O',],
# ] 
# Board.print_board(move(board))