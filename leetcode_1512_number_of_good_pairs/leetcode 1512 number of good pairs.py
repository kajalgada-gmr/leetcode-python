class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        # good_pairs = []
        num_good_pairs = 0
        nums_dict = {}
        
        for ind, each_num in enumerate(nums):
            
            if each_num in nums_dict:
                num_good_pairs += nums_dict[each_num]
                nums_dict[each_num] += 1
                
            else:
                nums_dict[each_num] = 1
            
        return num_good_pairs
  
