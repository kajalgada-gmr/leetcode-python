import numpy as np

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        unique_paths = np.ones((m,n), dtype=int)
        
        for m_ind in range(1, m):
            for n_ind in range(1, n):
                unique_paths[m_ind][n_ind] = unique_paths[m_ind-1][n_ind] + unique_paths[m_ind][n_ind-1]
                
        return unique_paths[m-1][n-1]
        
