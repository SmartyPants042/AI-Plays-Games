from compress import compressor, decompressor
from Board import Board
import json

MAX = float('inf')

# retrives the tree trained on MCTS Algorithm
with open('tree_of_ai.json') as f:
    tree = json.load(f)

def move(board):

    Board.print_board(board)
    best_score = -MAX
    best_child = None
    for compressed_child in tree[compressor(board)]['children']:
        if best_score < tree[compressed_child]['score']:
            best_child = compressed_child

    Board.print_board(decompressor(best_child))
    return

board = [
    ['-', '-', '-', '-',],
    ['-', 'X', '-', '-',],
    ['-', 'X', '-', 'O',],
    ['-', 'X', '-', 'O',],
]
move(board)