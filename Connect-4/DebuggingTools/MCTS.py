# helper functions/classes
from Board import Board
from compress import compressor, decompressor

# utility functions
import math
import json
import time

MAX = float('inf')

iterations = 9999

# this guy will store all the nodes as the keys
# and all of its children as a list of values
tree = {}

# the balance between exploration 
# and exploitation. 
# > 1 favour exploration
# < 1 favour exploration
# ==1 keep it balanced 
CONSTANT = 2

def convert_to_dict(node):
    return {
        'score': node.score,
        'count': node.count,
        'children': [compressor(child.game_state) for child in node.children],
    }

# Each node of the Tree.
class Node():
    def __init__(self, game_state, maxiPlayer):
        # game state is the board representation of what 
        # this node is. starting node is init with 
        # game board init. Rest of the nodes are init with
        # board state, given by the action(s) taken to get to that state.
        self.game_state = game_state

        # The total score that this node
        # has returned yet (NOT THE AVERAGE)
        # AKA THE OVERALL CONFIDENCE OF THIS NODE
        self.score = 0 

        # Count of number of times this node's
        # children have been explored
        self.count = 0 

        # A list of all the children 
        # of the current node
        # given as (action_taken, new_node)
        self.children = []

        # Whether the node is maximizer or not
        self.maxiPlayer = maxiPlayer

        # the compressed representation used for storing
        self.compressed = compressor(self.game_state)

class MCTS():
    def upper_confidence_bound(node):
        """
        returns:
            the UCB score of the given node
        """

        # if the node is newly initiated,
        # this condition will get activated
        if node.count == 0:
            if node.maxiPlayer:
                return -float('inf')
            else:
                return +float('inf')

        # Exploitation Logic: If this node has given me 
        # good results before, it will give them again
        exploit = node.score/node.count

        # Exploration Logic: There may be better nodes than
        # the ones we have explored, giving us 
        # possibly greater rewards.
        explore = math.sqrt(math.log(iterations) / node.count)
    
        # Constant set above.
        return  exploit + CONSTANT*explore

    def get_best_child(node):
        """
        explores all the children of the current node
        returns the best scoring child.

        if the player is maximizer, we return the max
        if the player is minimizer, we return the min
        """
        best_child = None
        if node.maxiPlayer:
            best_score = -MAX
        else:
            best_score = MAX

        # iterate through all the children
        for child in node.children:
            score = MCTS.upper_confidence_bound(child)
            # finding the max scoring child
            if node.maxiPlayer:
                if(score > best_score):
                    best_score = score
                    best_child = child
            # finding the min scoring child
            else:
                if(score < best_score):
                    best_score = score
                    best_child = child
            
            # if any one of the children is uninitialised
            # we pick that in UCB, so we pick it here too.
            if abs(best_score) == float('inf'):
                break
        
        return best_child

    def generate_children(node):
        """
        generates children for a given leaf node
        by looking at current actions.
        
        inputs:
            node:
                the current leaf node
        returns:
            a list of all possible game states, aka, children
        """

        # flipping the polarity of the children
        maxiPlayer = not node.maxiPlayer

        # get me the actions for this particular player
        all_actions = Board.get_actions(node.game_state, maxiPlayer)

        children = []
        for action in all_actions:

            # create a new board
            new_game_state = Board.simulate_action(
                action, 
                maxiPlayer, 
                node.game_state
            )

            # init a new node
            child = Node(new_game_state, maxiPlayer)
            children.append(child) 

        return children

    def rollout(node):
        """
        plays out random moves till the end
        
        inputs:
            node:
                the current game state
        returns: 
            the final score of the game state

        NOTE: We don't case what actions are taken to 
        get there. They can be ANYTHING!
        """

        game_state = node.game_state
        maxiPlayer = node.maxiPlayer
        init_maxiPlayer = maxiPlayer
        evaluation_results = Board.evaluate(game_state)

        # NOTE: To flip the maxiPlayer before or after
        # creates no difference, as we just want the final
        # resilution of the game
        while evaluation_results == None:
            maxiPlayer = not maxiPlayer
            game_state = Board.simulate_action(
                Board.get_actions(game_state, maxiPlayer)[0],
                maxiPlayer,
                game_state
            )
            evaluation_results = Board.evaluate(game_state)
        
        # the game ends in a draw.
        # We score it as 0.
        if evaluation_results == 0:
            return 0
        
        # If the game is won by AI, score is +1
        # elif the game is lost, socre is -2
        if evaluation_results == 'O':
            return 1
        else:
            return -1

    # recursive master function
    def master(node):
        # THIS node is accessed
        node.count += 1
        
        # Base Cases:
        # #1 the game has ended due to someone winning
        # OR, 
        # #2 the current node has no children 
        # and is thus the leaf node (best)
        
        # BASE CASE #1
        results = Board.evaluate(node.game_state)
        if results != None:
            return MCTS.analysing_result(results)

        # BASE CASE #2
        if not len(node.children):
            # STEP 2: NODE EXPANSION
            node.children = MCTS.generate_children(node)
            
            # if can't be expanded(filled board)
            # or, can be expanded, but game-over
            if not len(node.children):
                return MCTS.analysing_result(results)

            tree[node.compressed] = convert_to_dict(node)

            # the best child could be any in this case, 
            # since all activate the base case of 
            # the UCB function
            best_child = MCTS.get_best_child(node)

            # STEP 3: ROLLOUT
            random_simulation_results = MCTS.rollout(best_child)
            return random_simulation_results

        # STEP 1: TREE TRAVERSAL
        # finding the best child
        # from the current node and appending it to the history
        best_child = MCTS.get_best_child(node)

        # recurse! and get me the updation delta
        delta = MCTS.master(best_child)

        # STEP 4: BACKPROPOGATION
        # update the score now,
        # added with the results from recursion
        node.score += delta

        # saving the node in the tree, along
        # with its children
        tree[node.compressed] = convert_to_dict(node)

        return delta

    def mcts(
        starting_board=Board.get_initial_state(),
        verbose=True,
        save_tree=False,
        iterations=iterations):
        """
        returns the best next state for the board, given the current state.

        input:
            starting_board:
                The board on which to perform the seach on.
            verbose:
                Whether to display the progress bars and execution times
                or not.
            save_tree:
                Saves the tree in JSON format for future retrieval,
                if needed.
            iterations:
                number of times to simulate the search. More the
                #iters, more the time it will take.
                Default set as 9999
        return:
            the final board with the best results from the simulation.
        """

        # marks the start of execution time
        start_time = time.process_time()

        start_node = Node(starting_board, False)

        # for displaying the progress-bar
        total_bar_length = 50

        # controls the number of times
        # we are playing this game, aka, 
        # the number of simulations
        for i in range(iterations):

            # for each iteration, we will store the best path
            # this search will give us, to find the 
            # immediate best action. 
            # (eh, just use the board state representations ...)
            MCTS.master(start_node)

            # for displaying the progress-bar
            done_bar_length = round(i/iterations*50)
            length_left = total_bar_length - done_bar_length

            if verbose:
                print(f"Progress: [{'='*done_bar_length + '>'+ ' '*length_left}]\r", end = "")
        if verbose:
            print()

        try:
            final_board = MCTS.find_the_one(compressor(start_node.game_state))
        except:
            final_board = starting_board

        if save_tree:
            with open("tree.json", 'w+') as f:
                json.dump(tree, f, indent=4)
        
        if verbose:
            MCTS.print_stats(start_time, final_board)
        return final_board

    def find_the_one(board):
        """
        board is the compressed key of the board

        returns the board of the best child
        """
        best_score = -MAX
        best_child = None
        for compressed_child in tree[board]['children']:
            score = tree[compressed_child]['score']
            if best_score < score:
                best_child = compressed_child
                best_score = score
        
        best_board = decompressor(best_child)
        return best_board

    def print_stats(start_time, final_board):
        # Statistics
        print(f"Explored: {len(tree)} nodes")
        time_taken = round(time.process_time() - start_time, 2)
        print(f"Taken {time_taken}s to Execute")
        try:
            print("Best Score: ", tree[compressor(final_board)]['score'])
        except:
            print("Node remains unexplored, since game-over")
        return

    def analysing_result(results):
        """
        returns the score according to the evaluations
        """
        if results == None:
            return None

        # draw        
        if results == 0:
            return 0
        # AI wins
        if results == 'O':
            return 1
        # player wins
        return -1

################### TESTING ZONE ####################
# if __name__ == "__main__":
#     board = [
#         ['-', '-', '-', '-',],
#         ['-', 'X', '-', '-',],
#         ['-', 'X', '-', 'O',],
#         ['-', 'X', '-', 'O',],
#     ]  
#     Board.print_board(MCTS.mcts(starting_board=board, verbose=True, save_tree=True))

    # key = compressor(board)
    # print(key)
    # while key:
    #     Board.print_board(board)
    #     board = MCTS.find_the_one(key)
    #     key = compressor(board)
