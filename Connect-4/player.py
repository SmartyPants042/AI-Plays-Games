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
            
        num = -1
        while not(0 <= num <= dim_x-1):
            num = int(input(f"Input # between 1 and {dim_x}: "))-1

        for action in actions:
            if action[1] == num:
                board[action[0]][action[1]] = symbol
                return board

        print("Not available!")
        continue
    
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