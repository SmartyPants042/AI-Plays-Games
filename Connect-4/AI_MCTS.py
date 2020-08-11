from MCTS import MCTS
from Board import Board

def move(board, player_x=False):
    return MCTS.main(
        board,
        verbose='v',
        human_player=player_x,
        time_controlled=True,
        time_given=0.01)
    
################### TESTING ZONE ####################

# board = [
#     ['-', '-', '-', '-',],
#     ['-', 'X', '-', '-',],
#     ['-', 'X', '-', 'O',],
#     ['-', 'X', '-', 'O',],
# ] 
# Board.print_board(move(board))