Leetcode 617 Merge two binary trees

Problem Link: https://leetcode.com/problems/merge-two-binary-trees/

Solution Python:
+ We will merge both trees into the first one.
+ Observe each node at a time and create a stack of each node to assess.
    + Add the node values and assess their left and right nodes.
    + If a node exists on both tree, add it to be assessed.
    + If a node exists on just one tree:
        + If it exists on tree 1 and not tree 2, leave it as it is.
        + if it doesn't exist on tree 1 and exists on tree 2, add node from tree 2 to tree 1.
        + Once done, no need to evaluate this nodes children, they will remain unaffected.
