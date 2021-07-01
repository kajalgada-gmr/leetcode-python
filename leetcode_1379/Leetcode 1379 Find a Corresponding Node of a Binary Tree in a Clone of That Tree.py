# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        if cloned is None:
            return cloned
        
        nodes_explore = [[original, cloned]]
        res = None
        
        while nodes_explore:
            
            org_node, clone_node = nodes_explore.pop(0)
            
            if org_node is target:
                res = clone_node
                break
            
            else:
                if org_node.left:
                    nodes_explore.append([org_node.left, clone_node.left])
                    
                if org_node.right:
                    nodes_explore.append([org_node.right, clone_node.right])
                
        return res
                
