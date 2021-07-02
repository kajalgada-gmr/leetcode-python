Leetcode 1021. Remove Outermost Parentheses

Leetcode problem link: https://leetcode.com/problems/remove-outermost-parentheses/

Solution:
+ keep a track of 1st open parentheses.
+ find the end.
+ Then slice everything between the parentheses.

Slicing -> list[start:end]  -> includes start but not the end.
