# Connect 4
Players: 2
Information: Perfect Information
Dimensions: 7 columns x 6 rows

## Playing
### Execute:
`foo@bar:~/path/to/folder$ python3 main.py`

### There are few different options to get started!
![Main Menu](./Images/Menu.png)

### For Algorithms, You can select 'levels'
![Minimax Levels](./Images/MinimaxLevels.png)

## You can have one algorithm play against the other
![Minimax vs MCTS](./Images/MinimaxVMCTS.png)

### You can also have an algo play against itself!
![MCTS vs MCTS](./Images/MCTSvMCTS.png)

## Dependencies
None, written in vanilla Python3

## Code Structure
- Board:
    Handles all functions related to the board; from getting current valid moves, to the evaluation functions.

- main:
    The main file
- MCTS, Minimax:
    The Algorithms
- AI_MCTS, AI_Minimax, player
    Helper functions for the algorithms

## Algorithms
To be added soon ...
