from Board import Board

import time
import random
import math

MAX = float('inf')
SCALAR = 1
ITERATIONS = 969

class Node():
    def __init__(self, board, maxiPlayer):
        self.game_state = board
        self.maxiPlayer = maxiPlayer
        self.children = []

        self.count = 0        
        self.score = 0        

class MCTS():
    def ucb(node):
        """
        Returns the Upper Confidence Bound Score of the node.

        input:
            node:
                the Node object
        return:
            None if the node is unexplored
            value if the node is explored
        """
        if node.count == 0:
            return None

        explore = math.sqrt(math.log(ITERATIONS) / node.count)
        exploit = node.score/node.count
        return exploit + SCALAR*explore

    def get_best_child(node):
        """
        Returns the best child of the node according to the
        node being a maximizer/minimizer

        input:
            node:
                the Node object
        return:
            the best child for that particular node
        """
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
        """
        Takes a random series of moves from the given node,
        till the game ends: either in a win/loss or a draw.
        
        input:
            node:
                the Node object
        return:
            the analysis of the end-game-state results
        """
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
        """        
        Used for extracting out the Board's generic evaluation
        function.
        """
        if results == None:
            return None
        if results == 0:
            return -1
        if results == 'X':
            return -2
        return 1

    def generate_children(node):
        """
        Generates new child nodes for the given node
        input:
            node:
                the Node object
        return:
            None
        """
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
        """
        The main recursive function, follows the steps of
        
        1. Traversing the tree:
                If the current node has children already, 
                then we can pick the best one of them (according
                to the UCB scoring). And then, recurse further,
                till we reach a leaf-node. That leaf will be the best
                of that particular iteration.

        2. Expanding new children nodes:
                (explained above)
        
        3. Rollout:
                (explained above)
        
        4. Backpropogation:
                When it reaches an end-game-state, it returns the
                analysed evaluations of the board, 
        """

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

    def main(board=Board.get_initial_state(), verbose="v", human_player=False):
        """
        The function that controls it all.
        input:
            board:
                the board to get a new move on. Is init with
                the Board's function (if needed)
            verbose:
                '' - no output on the screen
                'v' - displays the progress bar
                'vv' - displays the scores of each of the
                    immediate board states
            human_player:
                False for AI playing, 
                True for Human playing 
                (can be used for self-play game-simulations.)
        return:
            the best future board, having the maximum score.

        NOTE:
            the start_node is essentially the minimizer node, 
            but letting it control means that the nodes with lesser
            values get explored more. So, we basically iterate over
            all of its children, and then get their max.
        """
        start_time = time.process_time()
        
        start_node = Node(board, human_player)
        MCTS.generate_children(start_node)
        new_start_nodes = start_node.children

        for i in range(ITERATIONS):
            for start in new_start_nodes:
                MCTS.recurse(start)
            if verbose == "v" or verbose == "vv":
                done_bar_length = round(i/ITERATIONS*50)
                length_left = 50 - done_bar_length
                print(f"Progress: [{'='*done_bar_length + '>'+ ' '*length_left}]\r", end = "")
        
        if verbose == "v" or verbose == "vv":
            print()

        best_child = None
        if not human_player:
            best_score = -MAX
        else:
            best_score = MAX

        for child in start_node.children:
            # Board.print_board(child.game_state)
            
            if verbose == "vv":
                print(child.score, child.count)

            if not human_player:
                if child.score > best_score:
                    best_score = child.score
                    best_child = child
            else:
                if child.score < best_score:
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
# Board.print_board(MCTS.main(board=board, verbose='v'))