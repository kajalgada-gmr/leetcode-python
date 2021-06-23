# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        res_decimal = 0
        while head:
            res_decimal = res_decimal*2 + head.val
            head = head.next
            
        return res_decimal
        
