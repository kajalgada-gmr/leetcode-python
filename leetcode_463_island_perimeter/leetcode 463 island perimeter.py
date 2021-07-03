class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        perimeter = 0
        rows = len(grid)
        cols = len(grid[0])
        
        for r_ind in range(rows):
            for c_ind in range(cols):
                
                if grid[r_ind][c_ind]:
                    perimeter += 4
                    
                    if (r_ind < (rows-1)) and grid[r_ind+1][c_ind]:
                        perimeter -= 1
                        
                    if (r_ind > 0) and grid[r_ind-1][c_ind]:
                        perimeter -= 1
                        
                    if (c_ind < (cols-1)) and grid[r_ind][c_ind+1]:
                        perimeter -= 1
                        
                    if (c_ind > 0) and grid[r_ind][c_ind-1]:
                        perimeter -= 1
                        
        return perimeter
