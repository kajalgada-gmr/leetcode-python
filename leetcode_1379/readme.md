Leetcode 1379 Find a Corresponding Node of a Binary Tree in a Clone of That Tree

Problem Link: https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

Solution:
+ This question is more about tree transversal.
+ Since the problem mentions all values are unique, one can simply search for target value and return the node.
+ A better way to do is loop through nodes. Keep a stack of original node and clone node.
  + for each orginal node compare to target. if match return the clone node.
  + else store original node left and right along with clone node left and right in stack.

