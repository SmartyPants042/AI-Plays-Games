class Board():
    """
    Provides Utility functions for the board.
    """
    @staticmethod
    def get_actions(board):
        """
        returns a list of tuples of (i, j) positions
        empty in the board.
        """
        actions = []
        # taking the transpose
        transpose = [[ board[i][j] for i in range(len(board))] for j in range(len(board[0]))]
        # transpose = list(map(list, zip(*board)))

        # finding the empty cells
        for i in range(len(transpose)):
            for j in reversed(range(len(transpose[0]))):
                if transpose[i][j] == '-':
                    actions.append((j,i))
                    break

        # done
        return actions

    @staticmethod
    def evaluate(board):
        """
        returns the winner if any, else None
        """
        
        # check rows
        for i in range(len(board)):
            for j in range(len(board[0]) - 3):
                if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] and board[i][j] != '-':
                    return board[i][j]

        # checking columns
        for i in range(len(board)-3):
            for j in range(len(board[0])):
                if board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] and board[i][j] != '-':
                    return board[i][j]

        # checking diagonal type 1
        for i in range(len(board)-3):
            for j in range(len(board[0])-3):
                if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] and board[i][j] != '-':
                    return board[i][j]

        # checking diagonal type 2
        for i in range(len(board)-3):
            for j in range(len(board[0])-3):
                if board[i+3][j] == board[i+2][j+1] == board[i+1][j+2] == board[i][j+3] and board[i][j+3] != '-':
                    return board[i][j+3]

        return None

    @staticmethod
    def print_board(board):
        """
        prints out the given board.
        """
        for row in board:
            print("| ", end="")
            for item in row:
                print(item, " | ", end="")
            print()
        
        return

    @staticmethod
    def get_board_size(board):
        # returns the board size for MCTS's saving part
        return (len(board), len(board[0]))

#################### TESTING ZONE ####################
# board = [
#     ['-', '-', '-', 'X', '-'],
#     ['-', '-', '-', 'X', '-'],
#     ['-', '-', 'O', 'X', '-'],
#     ['-', 'O', 'X', 'O', '-'],
#     ['-', 'O', 'X', 'X', '-'],
# ]
# print(Board.get_actions(board))