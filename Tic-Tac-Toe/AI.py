from Board import Board
import copy
import random

MAX = float('inf')

class AI():
    def minimax(maxiPlayer, depth_left, board, alpha, beta):
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
        
        # termination condition
        # (final_score, game_over) = evaluate(board)
        winner = Board.evaluate(board)
        if not depth_left or not winner:
            # if final_score:
            #     print(final_score, board)
            return 1 if winner == 'O' else -1 

        # calculate the possible future states
        children = Board.get_actions(board)

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
                new_board[child[0]][child[1]] = 'O'
            else: # which is user
                new_board[child[0]][child[1]] = 'X'

            # find present child's score
            score = AI.minimax((not maxiPlayer), depth_left-1, new_board, alpha, beta)

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


    def move(board, level=4):
        """
        Makes a move using the the algorithm.
        Does the first initial 'play' of the algorithm.
        """

        # game logic
        copy_board = copy.deepcopy(board)
        children = Board.get_actions(copy_board)
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
            new_copy_board[child[0]][child[1]] = 'O'

            score = AI.minimax(False, level, new_copy_board, -MAX, +MAX)
            
            print(score)

            if score == 1:
                ai_win.append(child)
            elif score == -1:
                player_win.append(child)
            else:
                hmm.append(child)

        count_player_win = len(player_win)
        count_ai_win = len(ai_win)
        count_hmm = len(hmm)

        if count_ai_win:
            best_move = random.choice(ai_win)
        elif count_hmm:
            best_move = random.choice(hmm)
        else:
            best_move = random.choice(player_win)
        print(board, best_move, best_score)
        return best_move

#################### TESTING ZONE ####################
# board = [
#     ['X', '-', 'O'],
#     ['-', 'X', '-'],
#     ['O', 'X', 'O'],
# ]
# print(AI.move(board))