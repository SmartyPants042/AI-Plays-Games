from Board import Board

import time
import random
import math
MAX = float('inf')
SCALAR = 0.1
ITERATIONS = 696

class Node():
    def __init__(self, board, maxiPlayer):
        self.game_state = board
        self.maxiPlayer = maxiPlayer
        self.children = []

        self.count = 0        
        self.score = 0        

class MCTS():
    def ucb(node):
        if node.count == 0:
            return None

        explore = math.sqrt(math.log(ITERATIONS) / node.count)
        exploit = node.score/node.count
        return exploit + SCALAR*explore

    def get_best_child(node):
        best_child = None
        if node.maxiPlayer:
            best_score = -MAX
        else:
            best_score = +MAX

        for child in node.children:
            score = MCTS.ucb(child)

            if score == None:
                best_child = child
                break
            if node.maxiPlayer:
                if score > best_score:
                    best_score = score
                    best_child = child
            else:
                if score < best_score:
                    best_score = score
                    best_child = child
        
        return best_child

    def rollout(node):
        board = node.game_state
        results = Board.evaluate(board)
        maxiPlayer = node.maxiPlayer

        while results == None:
            action = random.choice(Board.get_actions(board, maxiPlayer))
            maxiPlayer = not maxiPlayer
            board = Board.simulate_action(action, maxiPlayer, board)
            results = Board.evaluate(board) 

        return MCTS.analyse_results(results)

    def analyse_results(results):
        if results == None:
            return None
        if results == 0:
            return -1
        if results == 'X':
            return -2
        return 1

    def generate_children(node):
        actions = Board.get_actions(node.game_state, node.maxiPlayer)
        children = []
        maxiPlayer = not node.maxiPlayer

        for action in actions:
            children.append(
                Node(
                    Board.simulate_action(
                        action,
                        maxiPlayer,
                        node.game_state),
                    maxiPlayer)
            )

        node.children = children
        return

    def recurse(node):
        results = Board.evaluate(node.game_state)
        if results != None:
            delta = MCTS.analyse_results(results)

            if node.score == None:
                node.score = delta
            else:
                node.score += delta
            node.count += 1
            return delta
        
        if node.children:
            best_child = MCTS.get_best_child(node)
            delta = MCTS.recurse(best_child)
        else:
            MCTS.generate_children(node)
            best_child = MCTS.get_best_child(node)
            delta = MCTS.rollout(best_child)
            best_child.score = delta
            best_child.count += 1
            return delta
        
        node.score += delta
        node.count += 1
        return delta

    def main(board=Board.get_initial_state(), verbose=True):
        start_time = time.process_time()
        
        start_node = Node(board, False)
        MCTS.generate_children(start_node)
        new_start_nodes = start_node.children

        for i in range(ITERATIONS):
            for start in new_start_nodes:
                MCTS.recurse(start)
            if verbose:
                done_bar_length = round(i/ITERATIONS*50)
                length_left = 50 - done_bar_length
                print(f"Progress: [{'='*done_bar_length + '>'+ ' '*length_left}]\r", end = "")
        
        if verbose:
            print()

        best_child = None
        best_score = -MAX
        for child in start_node.children:
            # Board.print_board(child.game_state)
            
            if verbose:
                print(child.score, child.count)

            if child.score > best_score:
                best_score = child.score
                best_child = child

        return best_child.game_state

#################### TESTING ZONE ####################
# board = [
#     ['-', '-', '-', '-', '-'],
#     ['-', '-', '-', '-', '-'],
#     ['-', 'X', '-', '-', '-'],
#     ['-', 'X', '-', 'O', '-'],
#     ['-', 'X', '-', 'O', '-'],
# ]  
# MCTS.main(board=board, verbose=True)