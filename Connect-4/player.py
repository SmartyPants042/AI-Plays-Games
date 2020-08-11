from Board import Board

def move(board, player_x=True, level=0):

    dim_x = len(board[0])
    num = int(input(f"Input # between 1 and {dim_x}: "))-1
    actions = Board.get_actions(board, False)
    
    symbol = 'X' if player_x else 'O'

    for action in actions:
        if action[1] == num:
            board[action[0]][action[1]] = symbol
            return board
