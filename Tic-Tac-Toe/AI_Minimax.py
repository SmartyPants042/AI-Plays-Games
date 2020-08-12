from Board import Board
from Minimax import AI

def move(board, player_x=True, level=3):
    """
    returns the new board after the best move from minimax

    inputs:
        board:
            the current board state
        player_x:
            whether user inputs a 'X' or an 'O'
        level:
            search depth for minimax
    return:
        the new board with the new move.
    """
    # assuming the case that human_player == True ONLY.

    action = AI.move(board, player_x=player_x, level=level)
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