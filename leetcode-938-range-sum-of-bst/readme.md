Leetcode 938 range sum of BST

Problem link: https://leetcode.com/problems/range-sum-of-bst/

Solution:
+ Start with root.
+ If the number is within limits, add it to the final sum.
+ In BST, all numbers on right are higher than current number and all numbers on left are lower than current number.
+ Because we care about numbers within limit, if current number is lower than higher limit, we can look at numbers on right.
+ Similarly for other side.

