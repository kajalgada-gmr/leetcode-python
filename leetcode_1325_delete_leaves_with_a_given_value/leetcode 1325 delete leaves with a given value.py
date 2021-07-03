# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        
        if not root:
            return root
        
        if (root.left is None) and (root.right is None):
            if root.val == target:
                root = None
            return root
        
        nodes_target_val = []
        nodes_explore = []
        
        if root.left:
            nodes_explore.append([root, 'left', root.left])
            
        if root.right:
            nodes_explore.append([root, 'right', root.right])
        
        while nodes_explore:
            
            par, par_dir, cur_node = nodes_explore.pop(0)
            
            if cur_node.val == target:
                nodes_target_val.append([par, par_dir, cur_node])
                
            if cur_node.left:
                nodes_explore.append([cur_node, 'left', cur_node.left])
                
            if cur_node.right:
                nodes_explore.append([cur_node, 'right', cur_node.right])
                
        while nodes_target_val:
            
            par, par_dir, cur_node = nodes_target_val.pop()
            
            # Is it a leaf?
            if (cur_node.left is None) and (cur_node.right is None):
                if par_dir is 'left':
                    par.left = None
                else:
                    par.right = None
                    
        if (root.left is None) and (root.right is None) and (root.val == target):
            root = None
            
        return root
