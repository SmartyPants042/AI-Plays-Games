from Board import Board
import math

MAX = float('inf')

iterations = 1

# the balance between exploration 
# and exploitation. 
# > 1 favour exploration
# < 1 favour exploration
# ==1 keep it balanced 
CONSTANT = 2

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

class MCTS():
    def upper_confidence_bound(node):
        """
        returns:
            the UCB score of the given node
        """

        # if the node is newly initiated,
        # this condition will get activated
        if node.count == 0:
            return float('inf') 

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

        if not (node.children):
            # print("Initialising node's children myself ... ")
            node.children = generate_children(node)
            # print("Done!")

        # iterate through all the children
        for child in node.children:
            score = upper_confidence_bound(child)

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
            given as tuple of (actions, nodes_generated_by_them)
            And, the board generated will be depending upon
            whether the child is maximizer or a minimizer
        """

        # flipping the polarity of the children
        maxiPlayer = not self.maxiPlayer
        all_actions = get_actions()
        children = []
        for action in all_actions:
            new_game_state = Board.simulate_action(
                action, 
                maxiPlayer, 
                node.game_state
            )
            child = Node(new_game_state, maxiPlayer)
            children.append(child) 

        return children

    def rollout(node):
        """
        plays out random moves till the end
        
        inputs:
            node:
                the current game state
            maxiPlayer:
                is the current node maximizer or
                minimizer
        returns: 
            the final score of the game state

        NOTE: We don't case what actions are taken to 
        get there. They can be ANYTHING!
        """
        pass

    # recursive master function
    def master(node):
        # THIS node is accessed
        node.count += 1
        
        # Base Case:
        # the current node has no children 
        # and is thus the leaf node (best)
        if not len(node.children):
            # STEP 2: NODE EXPANSION
            node.children = generate_children(node)
            
            # the best child could be any in this case, 
            # since all activate the base case of 
            # the UCB function
            best_child = get_best_child(node)

            # STEP 3: ROLLOUT
            random_simulation_results = rollout(best_child)
            return random_simulation_results

        # STEP 1: TREE TRAVERSAL
        # finding the best child
        # from the current node and appending it to the history
        best_child = get_best_child(node)
        

        # recurse! and get me the updation delta
        delta = master(best_child)
        
        # STEP 4: BACKPROPOGATION
        # update the score now,
        # added with the results from recursion
        node.score += delta
        return delta

def mcts():
    start = Node()

    # controls the number of times
    # we are playing this game, aka, 
    # the number of simulations
    for i in range(iterations):

        # for each iteration, we will store the best path
        # this search will give us, to find the 
        # immediate best action. 
        # (eh, just use the board state representations ...)
        MCTS.master(start)

    # dump start node to a file for later use.
    # save it with particular board size configuration ...
