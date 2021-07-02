# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        if root is None:
            return TreeNode(val=val)
        
        cur_node = root
        
        while True:
            
            if cur_node.val < val:
                if cur_node.right:
                    cur_node = cur_node.right
                else:
                    cur_node.right = TreeNode(val=val)
                    break
                    
            else:
                if cur_node.left:
                    cur_node = cur_node.left
                else:
                    cur_node.left = TreeNode(val=val)
                    break

        return root
        
