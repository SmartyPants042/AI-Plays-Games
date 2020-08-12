# A Note to future self.
To implement the MCTS Algorithm in games such as Chess/Go,
we need a policy and value network (combined into one, like
the implementation of AlphaGo Zero.)
*Learns entirely from self play*

## Here's the Network Description:
1. Input the board state
2. Using ConvNets and ResNets to get a final possible states of boards (say, K boards).
3. These K boards are then put in MCTS as the maximizers, each will go through their separate simulation, which runs in the parallel.
4. All the K boards will have some score at the end, and we will choose the MAX of all of them.

~~We also somehow integrate the policy and value networks ... Not sure about that right now.~~

UPDATE:

Include the value and policy network evaluations in the Board.evalutae() method.

BONUS: 
- The AlphaGo team ran the MCTS simulations for 1600 Iterations!
- While the NNs are powerful on their own, (especially with the dual Policy + Value Networks) they still rely on MCTS for that boost in greatness.
- This *only* applies to perfect information games.
- Notice that the NN just replaces the start node of the MCTS.
rest all  remains the same.

RESOURCES:
- (Video) [AlphaGo & Deep Learning - Computerphile](https://www.youtube.com/watch?v=qWcfiPi9gUU)
- (Video) [How AlphaGo Zero works - Google DeepMind](https://www.youtube.com/watch?v=MgowR4pq3e8)
- (Article) [A Simple Alpha(Go) Zero Tutorial](https://web.stanford.edu/~surag/posts/alphazero.html)
- (Paper) [Mastering the Game of Go](https://www.nature.com/articles/nature24270.epdf?author_access_token=VJXbVjaSHxFoctQQ4p2k4tRgN0jAjWel9jnR3ZoTv0PVW4gB86EEpGqTRDtpIz-2rmo8-KG06gqVobU5NSCFeHILHcVFUeMsbvwS-lxjqQGg98faovwjxeTUgZAUMnRQ)