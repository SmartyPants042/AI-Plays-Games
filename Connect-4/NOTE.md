# A Note to future self.
To implement the MCTS Algorithm in games such as Chess/Go,
we need a policy and value network (combined into one, like
the implementation of AlphaGo Lee.)
*Learns entirely from self play*

## Here's the Network Description:
1. Input the board state
2. Using ConvNets and ResNets to get a final possible states of boards (say, K boards).
3. These K boards are then put in MCTS as the maximizers, each will go through their separate simulation, which runs in the parallel.
4. All the K boards will have some score at the end, and we will choose the MAX of all of them.

We also somehow integrate the policy and value networks ... Not sure about that right now.