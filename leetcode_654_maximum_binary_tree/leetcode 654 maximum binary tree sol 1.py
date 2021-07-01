# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        
        len_nums = len(nums)
        
        if len_nums == 0:
            return None
        elif len_nums == 1:
            return TreeNode(val=nums[0])
        
        stack = []
        last = None
        
        for cur_num in nums:
            
            while stack and (stack[-1].val < cur_num):
                last = stack.pop()
                
            cur_node = TreeNode(val=cur_num)
            if stack:
                stack[-1].right = cur_node
            if last:
                cur_node.left = last
                
            stack.append(cur_node)
            last = None
        
        return stack[0]
    
