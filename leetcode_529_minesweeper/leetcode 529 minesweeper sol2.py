class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        cr = click[0]
        cc = click[1]
        
        # If mine, return X
        if board[cr][cc] is 'M':
            board[cr][cc] = 'X'
            return board
        
        # Else if unrevealed empty tile, explore it
        elif board[cr][cc] is 'E':
            
            nodes_explore = [[cr, cc]]
            rows = len(board)
            cols = len(board[0])
            
            # Look at all the neighbours
            while nodes_explore:
                r, c = nodes_explore.pop(0)
                
                # If it is an empty unrevealed tile, check neighbours
                if board[r][c] is 'E':
                    num_mines = 0
                    tmp_nodes_explore = []
                    
                    # Add any number of mines in neighbours and keep track of unexplored neighbours
                    for r_ind in [r-1, r, r+1]:
                        for c_ind in [c-1, c, c+1]:
                            
                            if (0 <= r_ind < rows) and (0 <= c_ind < cols):
                                if board[r_ind][c_ind] is 'E':
                                    tmp_nodes_explore.append([r_ind, c_ind])
                                elif board[r_ind][c_ind] is 'M':
                                    num_mines += 1
                    
                    # If no mines, mark it clear and add neighbours to explore
                    if num_mines == 0:
                        board[r][c] = 'B'
                        nodes_explore += tmp_nodes_explore
                        
                    # else add number of mines
                    else:
                        board[r][c] = str(num_mines)    
        
        return board
