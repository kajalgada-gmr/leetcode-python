class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        start_loc = 0
        cur_count = 0
        new_s = ""
        
        for ind, each_char in enumerate(s):
            
            if each_char is "(":
                cur_count += 1
                
            elif each_char is ")":
                cur_count -= 1
                
            if cur_count == 0:
                new_s += s[start_loc+1:ind]
                start_loc = ind+1
                
        return new_s
