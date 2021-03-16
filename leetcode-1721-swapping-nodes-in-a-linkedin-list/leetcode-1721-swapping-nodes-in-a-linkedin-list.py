# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        
        # If it is a empty list or just has one node.
				if head is None or head.next is None:
            return head
        
        # LL index starts at 1. Go ahead (k-1) times to get to k node
        k_node = head
        for _ in range(1, k):
            k_node = k_node.next
        
        # If list had k nodes, 1st node (head) will be kth node from end      
        k_end_node = head
        
        # Keep going till end of list and move k_end_node one step ahead.
        cur_node = k_node
        while cur_node.next is not None:
            cur_node = cur_node.next
            k_end_node = k_end_node.next
            
        # Swap
        temp_val = k_node.val
        k_node.val = k_end_node.val
        k_end_node.val = temp_val
        
        return head
