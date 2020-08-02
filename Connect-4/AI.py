from MCTS import MCTS

def move(board):
    return MCTS.mcts(board, save_tree=True)
