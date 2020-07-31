class Board():
    def __init__(self, level=0):
        # the 3x3 board
        self.board = [['-'] * 3] * 3

        # our representation of the player
        self.player = 'X'
        # our representation of the AI
        self.ai = 'O'
        # level of AI
        self.level = level
        return

    def get_actions(self):
        """
        returns a list of tuples of i, j positions
        empty in the board
        """
        board = self.board
        actions = []
        # finding the empty cells
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '-':
                    actions.append((i,j))
        # done
        return actions

    def evaluate(self):
        """
        returns the winner if any, else None
        """
        board = self.board
        
        # row scan
        for i in range(len(board)):
            if (board[i][0] == board[i][1] == board[i][2]) and (board[i][0] != '-'):
                return board[i][0]
        # column scan
        for i in range(len(board)):
            if (board[0][i] == board[1][i] == board[2][i]) and (board[0][i] != '-'):
                return board[i][0]
        # primary diagonal
        if (board[0][0] == board[1][1] == board[2][2]) and (board[1][1] != '-'):
            return board[0][0]
        # secondary diagonal
        if (board[2][0] == board[1][1] == board[0][2]) and (board[1][1] != '-'):
            return board[2][0]
            
        # Couldn't find any winner
        return None

    def print_board(self):
        """
        prints out the current state of the board.
        """
        for row in self.board:
            print("| ", end="")
            for item in row:
                print(item, " | ", end="")
            print()
        
        return

#################### TESTING ZONE ####################
# game = Board()
# game.print_board()
# print(game.evaluate())
# print(game.get_actions())