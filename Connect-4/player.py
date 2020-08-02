from Board import Board

def move(board):

    dim_x = len(board[0])
    num = int(input(f"Input # between 1 and {dim_x}: "))-1
    actions = Board.get_actions(board, False)
    
    for action in actions:
        if action[1] == num:
            return action

    return None