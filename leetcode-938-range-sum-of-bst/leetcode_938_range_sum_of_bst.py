# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        
        nodes_to_explore = [root]
        sum_nodes = 0
        
        while nodes_to_explore:
            
            cur_node = nodes_to_explore.pop()
            cur_node_val = cur_node.val
            
            if (cur_node_val >= low) and (cur_node_val <= high):
                sum_nodes += cur_node_val
                
            if (cur_node_val < high) and (cur_node.right != None):
                nodes_to_explore.append(cur_node.right)
                
            if (cur_node_val > low) and (cur_node.left != None):
                nodes_to_explore.append(cur_node.left)
                
        return sum_nodes
            
