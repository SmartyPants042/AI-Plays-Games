from Board import Board
import copy
import random

MAX = float('inf')

class AI():
    @staticmethod
    def minimax(maxiPlayer, depth_left, board, alpha, beta, ai_symbol, opp_symbol):
        """
        The Minimax Algorithm with pruning.
        input params:
            maxiPlayer: Whether the player wants to maximize or
                minimize the score. Alternates with each call.
            depth_left: Dictates how much more deep
                the ai can search
            board: This is the 'to-be' state of the board given
                that particular choice of moves. *Passed by copy*.
            alpha, beta: Parameters set by the player maximizing
                the score and the player minimizing the score
                respectively. Prunes the search tree, reduces 
                the time complexity.
        output:
            The score.
            
            NOTE: This algorithm DOES NOT pick the best possible move.
            Instead, put another loop outside as the "first iteration
            through the possible moves". Select the best move according 
            to the result by the algorithm.
        """
        
        winner = Board.evaluate(board)

        if winner:
            return 1 if winner == ai_symbol else -1
        if not depth_left:
            return 0
        
        # calculate the possible future states
        children = Board.get_actions(board, maxiPlayer)

        # init
        if maxiPlayer:
            best = -MAX
        else:
            best = MAX

        # loop through possible states
        for child in children:
            
            # create a new board according to the 'child', aka
            # available empty cells
            new_board = copy.deepcopy(board)
            if maxiPlayer: # which is AI
                new_board[child[0]][child[1]] = ai_symbol
            else: # which is user
                new_board[child[0]][child[1]] = opp_symbol

            # find present child's score
            score = AI.minimax(
                            (not maxiPlayer), 
                            depth_left-1,
                            new_board,
                            alpha,
                            beta,
                            ai_symbol,
                            opp_symbol
                        )

            # store if the board state is worth it
            if maxiPlayer:
                best = max(best, score)
                aplha = max(alpha, best)
            else:
                best = min(best, score)
                beta = min(beta, best)

            # print(alpha, beta)
            # pruning condition
            if beta <= alpha:
                break
        
        # Yeet
        return best

    @staticmethod
    def move(board, level=2, player_x=True):
        """
        Makes a move using the the algorithm.
        Does the first initial 'play' of the algorithm,
        to extract the move, which the minimax actually hides.
        """
        # symbol logic
        ai_symbol = 'X' if player_x else 'O'
        opp_symbol = 'O' if player_x else 'X'

        # game logic
        copy_board = copy.deepcopy(board)
        children = Board.get_actions(copy_board, True)
        best_score = -MAX
        best_move = None

        # for the probability & randomness
        ai_win = []
        player_win = []
        hmm = []
        
        # loop through possible states
        for child in children:
            
            # create a new board according to the 'child', aka
            # available empty cells
            new_copy_board = copy.deepcopy(copy_board)
            new_copy_board[child[0]][child[1]] = ai_symbol

            score = AI.minimax(False, level, new_copy_board, -MAX, +MAX, ai_symbol, opp_symbol)
            
            if score == 1:
                ai_win.append(child)
            elif score == -1:
                player_win.append(child)
            else:
                hmm.append(child)

        # picks random moves from a given set of scores
        # to keep it interesting ;)
        if len(ai_win):
            best_move = random.choice(ai_win)
        elif len(hmm):
            best_move = random.choice(hmm)
        # THIS. IS. SO. SAD.
        else:
            best_move = random.choice(player_win)

        return best_move
