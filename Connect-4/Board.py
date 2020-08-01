import copy

class Board():
    """
    Provides Utility functions for the board.
    Assumes 'X' for Opponent
    Assumes 'O' for AI
    """

    @staticmethod
    def get_initial_state():
        """
        arranges all the pieces in their init positions 
        """
        board = [
            ['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-'],
        ]
        return board

    @staticmethod
    def get_actions(board, maxiPlayer):
        """
        returns a list of tuples of (i, j) positions
        empty in the board, according to C4.

        This is a case where we have no need to specify
        which player it is. but, for games such as chess,
        we will need it in the future...
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
        Returns -1 in case the board is filled
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

        filled = True
        for row in board:
            for i in row:
                if i == '-':
                    filled = False
                    break
            
            if not filled:
                break

        if filled:
            return -1
        else:
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
        print('====='*len(board[0]) + '=')
        return

    @staticmethod
    def get_board_size(board):
        # returns the board size for MCTS's saving part
        return (len(board), len(board[0]))

    @staticmethod
    def simulate_action(action, maxiPlayer, board):
        """
        returns the changes board state after
        performing the action.
        
        here, action is (any) one element of the list given
        by get_actions function.
        """
        new_board = copy.deepcopy(board)
        new_board[action[0]][action[1]] = 'O' if maxiPlayer else 'X'
        return new_board 

#################### TESTING ZONE ####################
# board = [
#     ['-', '-', '-', 'X', '-'],
#     ['-', '-', '-', 'X', '-'],
#     ['-', '-', 'O', 'X', '-'],
#     ['-', 'O', 'X', 'O', '-'],
#     ['-', 'O', 'X', 'X', '-'],
# ]
# print(Board.get_actions(board))