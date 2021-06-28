# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        
        # If either or both trees are empty
        
        if (root1 is None) and (root2 is None):
            return None
        
        elif root1 is None:
            return root2
        
        elif root2 is None:
            return root1
        
        # Combine trees into 1st tree
        stack_nodes = [[root1, root2]]
        
        while stack_nodes:
            
            cur_1, cur_2 = stack_nodes.pop()
            cur_1.val += cur_2.val
            
            # If both trees have a left node, add it to stack
            if (cur_1.left is not None) and (cur_2.left is not None):
                stack_nodes.append([cur_1.left, cur_2.left])
            
            # If tree 1 has a node and tree 2 doesn't, it remains unchanged.
            # If tree 1 doesn't have a node and tree 2 does, add tree 2 node to tree 1.
            elif cur_1.left is None:
                cur_1.left = cur_2.left
                
            if (cur_1.right is not None) and (cur_2.right is not None):
                stack_nodes.append([cur_1.right, cur_2.right])
                
            elif cur_1.right is None:
                cur_1.right = cur_2.right
                
        return root1
 
