# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        
        # Step 1: # Compute Length of Linkedin List
        len_ll = 0
        cur_node = root
        
        while cur_node is not None:
            len_ll += 1
            cur_node = cur_node.next
            
        result = []
        
        # Checkpoint: if linkedin list len is k or less, each part will have 1 node or None
        if len_ll <= k:
            cur_node = root
            for _ in range(k):
                if cur_node is not None:
                    result.append(ListNode(val=cur_node.val))
                    cur_node = cur_node.next  
                else:
                    result.append(None)
                
        # Checkpoint: else
        else:
                
            # Compute each part size
            len_part = int(len_ll/k)
            rem = len_ll%k
            
            # Create results
            prev_node = None
            curr_node = root
            result.append(curr_node)
            
            # First large parts
            for _ in range(rem):
                
                for _ in range(len_part+1):
                    prev_node = curr_node
                    curr_node = curr_node.next
                    
                prev_node.next = None
                result.append(curr_node)
            
            # rest small parts
            for _ in range(rem+1, k):
                
                for _ in range(len_part):
                    prev_node = curr_node
                    curr_node = curr_node.next
                    
                prev_node.next = None
                result.append(curr_node)
        
        return result
