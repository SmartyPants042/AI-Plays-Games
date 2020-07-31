from Board import Board
from AI import AI 

# variables init
player = True
board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-'],
]
level = 5

# main game loop
while True:
    Board.print_board(board)

    winner = Board.evaluate(board)
    if winner:
        print(winner, " has won!")
        break

    # onto the next move
    # user's turn
    if player:
        x, y = map(int, input("Input x, y (zero indexed): ").split())
        # error handling
        while board[x][y] != '-':
            x, y = map(int, input("Don't Overwrite! : ").split())
        board[x][y] = 'X'
    # ai's turn
    else:
        print("Thinking ... ", end="")
        best_move = AI.move(board, level)
        board[best_move[0]][best_move[1]] = 'O'
        print("Got it.")
    # switching the player
    player = not player
