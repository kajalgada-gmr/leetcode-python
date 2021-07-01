# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        if root is None:
            return 0
        elif (root.left is None) and (root.right is None):
            return 1
        
        min_depth = 1000000
        nodes = [[root, 1]]
        
        while nodes:
            
            cur_node, cur_depth = nodes.pop(0)
            
            if cur_depth > min_depth:
                continue
            
            if cur_node.left:
                # Check for leaf
                if (cur_node.left.left is None) and (cur_node.left.right is None):
                    min_depth = min(cur_depth + 1, min_depth)
                else:
                    nodes.append([cur_node.left, cur_depth + 1])
                    
            if cur_node.right:
                # Check for leaf
                if (cur_node.right.left is None) and (cur_node.right.right is None):
                    min_depth = min(cur_depth + 1, min_depth)
                else:
                    nodes.append([cur_node.right, cur_depth + 1])
                    
        return min_depth
