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
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '-':
                    actions.append((i,j))
        # done
        return actions

    @staticmethod
    def evaluate(board):
        """
        returns the winner if any, else None
        """
        
        # row scan
        for i in range(len(board)):
            if (board[i][0] == board[i][1] == board[i][2]) and (board[i][0] != '-'):
                return board[i][0]
        # column scan
        for i in range(len(board)):
            if (board[0][i] == board[1][i] == board[2][i]) and (board[0][i] != '-'):
                return board[0][i]
        # primary diagonal
        if (board[0][0] == board[1][1] == board[2][2]) and (board[1][1] != '-'):
            return board[0][0]
        # secondary diagonal
        if (board[2][0] == board[1][1] == board[0][2]) and (board[1][1] != '-'):
            return board[2][0]
            
        # Couldn't find any winner
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
