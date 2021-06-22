class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_dict = {}
        res = []
        
        for cur_ind, cur_num in enumerate(nums):
            
            rem_num = target - cur_num
            
            if rem_num in nums_dict:
                rem_ind = nums_dict[rem_num]
                res = [rem_ind, cur_ind]
                break
                
            nums_dict[cur_num] = cur_ind
            
        return res
        
