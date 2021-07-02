Leetcode Insert into a Binary Search Tree

Problem Link: https://leetcode.com/problems/insert-into-a-binary-search-tree/

Solution:
+ Rule: left side has smaller number and right side has bigger numbers
+ Start with root as current node
+ If current node value is smaller than value to add, go right. Else go left.
+ Continue going down the tree until you reach a leaf i.e. no node below it and you can the new value here.


