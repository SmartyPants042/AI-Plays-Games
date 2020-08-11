from MCTS import MCTS
from Board import Board

def move(board, player_x=False, level=3):
    return MCTS.main(
        board,
        verbose='v',
        human_player=player_x,
        time_controlled=True,
        time_given=level)
    
################### TESTING ZONE ####################

# board = [
#     ['-', '-', '-', '-',],
#     ['-', 'X', '-', '-',],
#     ['-', 'X', '-', 'O',],
#     ['-', 'X', '-', 'O',],
# ] 
# Board.print_board(move(board))