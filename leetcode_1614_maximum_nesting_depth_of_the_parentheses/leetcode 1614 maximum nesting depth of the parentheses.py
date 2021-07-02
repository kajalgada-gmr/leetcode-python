class Solution:
    def maxDepth(self, s: str) -> int:
        
        cur_num = 0
        max_num = 0
        
        for each_char in s:
            if each_char is "(":
                cur_num += 1
                max_num = max(max_num, cur_num)
                
            elif each_char is ")":
                cur_num -= 1
                
        return max_num
        
