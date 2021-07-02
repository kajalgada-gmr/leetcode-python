Leetcode 1614. Maximum Nesting Depth of the Parentheses

Problem link: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

Solution:
+ Keep it simple.
+ Have current count for current open-close pair and maximum for overall max.
+ Count num of open brackets as current count. Keep updating max
+ If you meet end of bracket, subtract one from current count

