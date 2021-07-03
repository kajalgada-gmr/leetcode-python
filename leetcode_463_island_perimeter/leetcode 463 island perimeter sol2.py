import numpy as np
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        perimeter = 0
        rows = len(grid)
        cols = len(grid[0])
        
        # Find first island square
        nodes_explore = [[0, 0]]
        nodes_explored = np.zeros((rows, cols), dtype=bool)
        island_found = False
        
        while nodes_explore and not island_found:
            
            r_ind, c_ind = nodes_explore.pop()
            
            if grid[r_ind][c_ind]:
                nodes_explore = [[r_ind, c_ind]]
                island_found = True
                
            else:
                nodes_explored[r_ind][c_ind] = 1
                
                if r_ind < (rows-1) and not nodes_explored[r_ind+1][c_ind]:
                    nodes_explore.append([r_ind+1, c_ind])
                    
                if c_ind < (cols-1) and not nodes_explored[r_ind][c_ind+1]:
                    nodes_explore.append([r_ind, c_ind+1])
                    
        while nodes_explore:
            
            r_ind, c_ind = nodes_explore.pop()
            
            # Check for duplicate entries in nodes_explore
            if not nodes_explored[r_ind][c_ind]:
                nodes_explored[r_ind][c_ind] = 1

                # Right
                if (r_ind < (rows-1)) and grid[r_ind+1][c_ind]:
                    if not nodes_explored[r_ind+1][c_ind]:
                        nodes_explore.append([r_ind+1, c_ind])
                else:
                    perimeter += 1

                # Left
                if (r_ind > 0) and grid[r_ind-1][c_ind]:
                    if not nodes_explored[r_ind-1][c_ind]:
                        nodes_explore.append([r_ind-1, c_ind])
                else:
                    perimeter += 1

                # Up
                if (c_ind > 0) and grid[r_ind][c_ind-1]:
                    if not nodes_explored[r_ind][c_ind-1]:
                        nodes_explore.append([r_ind, c_ind-1])
                else:
                    perimeter += 1


                # Down
                if (c_ind < (cols-1)) and grid[r_ind][c_ind+1]:
                    if not nodes_explored[r_ind][c_ind+1]:
                        nodes_explore.append([r_ind, c_ind+1])
                else:
                    perimeter += 1
        
        return perimeter
