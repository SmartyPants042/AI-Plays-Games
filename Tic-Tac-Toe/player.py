from Board import Board

def move(board, player_x=True, level=0):
    """
    Lets the user input stuff.
    inputs:
        board:
            the current board state
        player_x:
            whether user inputs a 'X' or an 'O'
        level:
            dummy variable
    return:
        the new board with the new move.
    """

    dim_x = len(board[0])
    actions = Board.get_actions(board, player_x)
    symbol = 'X' if player_x else 'O'
    
    while True:
        if not actions:
            return None

        x, y = map(int, input("Input x, y (zero indexed): ").split())
        try:
            while board[x][y] != '-':
                x, y = map(int, input("Don't Overwrite! : ").split())
        except:
            continue

        board[x][y] = symbol
        return board
    
# if __name__ == "__main__":
#     board = [
#         ['-', 'X', '-', '-', '-', '-', '-'],
#         ['-', 'O', '-', '-', '-', '-', '-'],
#         ['-', 'X', '-', '-', '-', '-', '-'],
#         ['-', 'O', '-', '-', '-', '-', 'X'],
#         ['X', 'O', 'O', 'O', '-', '-', 'X'],
#         ['O', 'X', 'X', 'O', '-', 'X', 'X'],
#     ]
#     print(move(board))