Leetcode 1721 Swapping Nodes in a Linked List

Link to leetcode problem: https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

Learnings:

- Swapping 2 nodes → you can simply swap their values. No need to change the pointers!
- Same as getting k nodes from back.
- If the list had k nodes and you want kth node from end, that is the first node (head). 
  
  So to kth node from end, go to kth node. 

  Then have a pointer to head as kth node from end
  and a pointer to kth node as current node.

  Move both till end of list.
