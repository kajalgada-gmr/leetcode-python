class Solution:
    
    def countNeg(self, row, col_start, row_len):
    
        # If start of row is negative, no point in checking
        if row[col_start] >= 0:
            
            col_end = row_len - 1
            while col_start < col_end:
                mid = col_start + ((col_end - col_start) // 2)
                if row[mid] < 0:
                    col_end = mid
                else:
                    col_start = mid + 1
            
        count = row_len - col_start
        return count, col_start
    
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        count = 0
        col_num = 0
        row_len = len(grid[0])
        
        # Loop through each loop, stop if row has all positive numbers.
        while grid and (grid[-1][-1] < 0):
            each_row = grid.pop()
            each_count, col_num = self.countNeg(each_row, col_num, row_len)
            count += each_count
                
        return count
