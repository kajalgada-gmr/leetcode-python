# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        
        # Check if root is leaf
        if root is None:
            return False
        
        if (root.left is None) and (root.right is None):
            if root.val == targetSum:
                return True
            else:
                return False
        
        # Look for path
        path_found = False
        nodes = [[root, root.val]]
        
        while nodes:
            
            cur_node, cur_sum = nodes.pop()
            
            # Check left node
            if cur_node.left:
                if (cur_node.left.left is None) and (cur_node.left.right is None):
                    if (cur_sum + cur_node.left.val) == targetSum:
                        path_found = True
                        break
                        
                else:
                    nodes.append([cur_node.left, cur_sum + cur_node.left.val])
                    
            # Check right node
            if cur_node.right:
                if (cur_node.right.left is None) and (cur_node.right.right is None):
                    if (cur_sum + cur_node.right.val) == targetSum:
                        path_found = True
                        break
                        
                else:
                    nodes.append([cur_node.right, cur_sum + cur_node.right.val])
        
        return path_found
        
