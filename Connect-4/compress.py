def compressor(board):
    """
    converts a board to its compressed respresentation
    """
    compressed_val = ""

    dim_y = len(board)
    dim_x = len(board[0])
    for i in range(len(board)):
        for j in range(len(board[i])):
            cell = board[i][j]
            if cell == '-':
                continue
            elif cell == 'O':
                compressed_val += str(i*dim_x*2+ j*2 + 1) + '.'
            else:
                compressed_val += str(i*dim_x*2 + j*2 + 2) + '.'
    
    return (str(dim_x) + '.' + str(dim_y) + '.' + compressed_val)

def decompressor(compressed):
    """
    returns the board representation of the compressed value
    """
    temp = compressed.split('.')
    dim_x = int(temp[0])
    dim_y = int(temp[1])

    temp = temp[2:]
    board = []

    # creating the dummy board
    for i in range(dim_y):
        row = []
        for j in range(dim_x):
            row.append('-')
        board.append(row)
    
    # adding the compressed-values
    for item in temp:
        try:
            item = int(item)
        except:
            continue
        cell = 'O'
        item -= 1

        if item&1:
            item -= 1    
            cell = 'X'
        
        item /= 2

        i = int(item//dim_x) 
        j = int(item % dim_x)

        board[i][j] = cell 

    return board
#################### TESTING ZONE ####################
# board = [
#     ['X', 'X', 'O'],
#     ['X', 'X', '-'],
#     ['O', 'X', '-'],
# ]
# key = compressor(board)
# print(key)
# print(decompressor(key))
