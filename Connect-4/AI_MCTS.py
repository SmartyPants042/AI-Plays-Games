from MCTS import MCTS
from Board import Board

def move(board, player_x=False, level=3):
    """
    returns the new board after the best move from mcts

    inputs:
        board:
            the current board state
        player_x:
            whether user inputs a 'X' or an 'O'
        level:
            the time given to search for mcts in seconds.
    return:
        the new board with the new move.
    """
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