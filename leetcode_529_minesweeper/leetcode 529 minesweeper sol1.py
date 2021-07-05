class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        cr = click[0]
        cc = click[1]
        
        if board[cr][cc] is 'M':
            board[cr][cc] = 'X'
            return board
        
        elif board[cr][cc] is 'E':
            nodes_explore = [[cr, cc]]
            rows = len(board)
            cols = len(board[0])
            
            while nodes_explore:
                r, c = nodes_explore.pop(0)
                
                if board[r][c] is 'E':
                    num = 0
                    tmp_nodes_explore = []
                    
                    # Right
                    if (r < (rows-1)):
                        if board[r+1][c] is 'E':
                            tmp_nodes_explore.append([r+1, c])
                        elif board[r+1][c] is 'M':
                            num += 1
                    
                    # Right-Down
                    if (r < (rows-1)) and (c < (cols-1)):
                        if board[r+1][c+1] is 'E':
                            tmp_nodes_explore.append([r+1, c+1])
                        elif board[r+1][c+1] is 'M':
                            num += 1 
                    
                    # Down
                    if (c < (cols-1)):
                        if board[r][c+1] is 'E':
                            tmp_nodes_explore.append([r, c+1])
                        elif board[r][c+1] is 'M':
                            num += 1
                            
                    # Left-down
                    if (r > 0) and (c < (cols-1)):
                        if board[r-1][c+1] is 'E':
                            tmp_nodes_explore.append([r-1, c+1])
                        elif board[r-1][c+1] is 'M':
                            num += 1
                            
                    # Left
                    if (r > 0):
                        if board[r-1][c] is 'E':
                            tmp_nodes_explore.append([r-1, c])
                        elif board[r-1][c] is 'M':
                            num += 1
                            
                    # Left-up
                    if (r > 0) and (c > 0):
                        if board[r-1][c-1] is 'E':
                            tmp_nodes_explore.append([r-1, c-1])
                        elif board[r-1][c-1] is 'M':
                            num += 1
                            
                    # Up
                    if (c > 0):
                        if board[r][c-1] is 'E':
                            tmp_nodes_explore.append([r, c-1])
                        elif board[r][c-1] is 'M':
                            num += 1
                            
                    # Right-up
                    if (r < (rows-1)) and (c > 0):
                        if board[r+1][c-1] is 'E':
                            tmp_nodes_explore.append([r+1, c-1])
                        elif board[r+1][c-1] is 'M':
                            num += 1
                            
                    if num == 0:
                        board[r][c] = 'B'
                        nodes_explore += tmp_nodes_explore
                    else:
                        board[r][c] = str(num)
                        
        
        return board
