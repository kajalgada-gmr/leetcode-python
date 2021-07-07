"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        
        # print(customfunction.f(1, 2))
        
        res = []
        lastx_sol = -1
        
        x = 0
        y = 0
        
        while (lastx_sol <= z) and (x <= 1000):
            
            x += 1
            lastx_sol = customfunction.f(x, 1)
            
            cur_sol = lastx_sol
            y = 0
            
            while (cur_sol <= z) and (y <= 1000):
                
                y += 1
                cur_sol = customfunction.f(x, y)
                
                if cur_sol is z:
                    res.append([x, y])
        
        return res
