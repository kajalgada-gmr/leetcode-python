# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        slow = head
        fast = head
        cycle_exists = False
        
        while (fast != None) and (fast.next != None):
            
            slow = slow.next
            fast = fast.next.next
            
            if (slow == fast):
                cycle_exists = True
                break
                
        return cycle_exists
       
