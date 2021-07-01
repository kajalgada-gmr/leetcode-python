Leetcode 654 Maximum Binary Tree

Problem Link: https://leetcode.com/problems/maximum-binary-tree/

Solution 1:
+ Keep a track of nodes.
+ Find the maximum, everything on right of max num is stored as new list and same for left.
+ Loop through:
  + for each sub list, find max number. Add it to previous node left/ right based on its postition.
  + Create new sub list of numbers on left and right of max number.

Cons with sol1 is high memory usage.
Solution 1 Link: https://github.com/KajalGada/leetcode-python/blob/main/leetcode_654_maximum_binary_tree/leetcode%20654%20maximum%20binary%20tree%20sol%201.py


Solution 2 Explaination: https://leetcode.com/problems/maximum-binary-tree/discuss/258364/Python-O(n)-solution-with-explanation.

Solution 2 Link: 
