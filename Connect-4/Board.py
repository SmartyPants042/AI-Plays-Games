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
        # finding the empty cells

        pass

        # done
        return actions

    @staticmethod
    def evaluate(board):
        """
        returns the winner if any, else None
        """
        
        # check rows
        for i in range(len(board)):
            for j in range(len(board[0] - 3)):
                if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] and board[i][j] != '-':
                    return board[i][j]

        # checking columns
        for i in range(len(board)-3):
            for j in range(len(board[0])):
                if board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] and board[i][j] != '-':
                    return board[i][j]

        # checking diagonal type 1
        for i in range(len(board)-3):
            for j in range(len(board[0]-3)):
                if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] and board[i][j] != '-':
                    return board[i][j]

        # checking diagonal type 2
        for i in range(len(board)-3):
            for j in range(len(board[0]-3)):
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

#################### TESTING ZONE ####################
board = [
    ['-', '-', '-', '-', '-'],
    ['-', '-', 'X', '-', '-'],
    ['-', '-', 'X', '-', '-'],
    ['-', '-', 'X', '-', '-'],
    ['-', '-', 'X', '-', '-'],
]

print(Board.evaluate(board))