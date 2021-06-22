class Solution:
      def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums_len = len(nums)
        
        if nums_len < 3:
            return []
        
        triplets = []
        nums.sort()
        
        target_ind = 0
        target_num = nums[target_ind]
        
        while (target_num < 1) and (target_ind < (nums_len - 2)):
                
            left_ind = target_ind + 1
            right_ind = nums_len - 1

            while left_ind < right_ind:

                left_num = nums[left_ind]
                right_num = nums[right_ind]

                three_sum = target_num + left_num + right_num

                if three_sum == 0:

                    triplets.append([target_num, left_num, right_num])

                    # Look for other triplet with same target num.

                    # Skip through duplicate left and right num
                    left_ind += 1
                    while (left_ind < right_ind) and (nums[left_ind] == left_num):
                        left_ind += 1
                        
                    right_ind -= 1
                    while (right_ind > target_ind) and (nums[right_ind] == right_num):
                        right_ind -= 1

                elif three_sum < 0:
                    
                    left_ind += 1
                    while (left_ind < right_ind) and (nums[left_ind] == left_num):
                        left_ind += 1

                else:
                    
                    right_ind -= 1
                    while (right_ind > target_ind) and (nums[right_ind] == right_num):
                        right_ind -= 1
                        
            target_ind += 1
            while (target_ind < nums_len - 2) and (nums[target_ind] == nums[target_ind - 1]):
                target_ind += 1
            target_num = nums[target_ind]
                 
        return triplets
