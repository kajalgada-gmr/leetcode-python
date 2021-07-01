Leetcode 112 Path Sum

Problem Link: https://leetcode.com/problems/path-sum/

Solution:
+ Check if root is not None and root is leaf.
+ Explore each node and keep a stack of nodes to explore.
  + check if node is leaf.
    + check if path found
  + else add node children to explore stack

