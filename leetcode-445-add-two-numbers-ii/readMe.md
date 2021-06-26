Leetcode 445 Add Two Numbers II

Problem link: https://leetcode.com/problems/add-two-numbers-ii/

Solution:
+ Given numbers are in reverse, just remove from linked list and add to a list.
+ Then pop from list and add them. Pop -> removes the last number.
+ Add and store as a linkedin list. Also track carry
+ We will build the linked list in reverse. So save added number as a new node and connect the linked list so far as next to new node.
+ Remember to add the carry to linked list in end.
