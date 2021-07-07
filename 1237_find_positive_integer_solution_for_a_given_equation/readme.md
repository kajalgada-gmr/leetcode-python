Leetcode 1237 Find Positive Integer Solution for a Given Equation

Problem link: https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/

Tip: Think of 2 pointer solutions!

Solution 1:
+ Try different combinations of x and y for solution.
+ Given when we increment x or y the solution becomes larger, we stop once we hit z.
+ So start with one value of x and loop through y till you get f(x,y) as z. Store values when you reach z, then reset y and increment x.

Solution 2:
+ 2 pointer approach i.e. two sum solution 1: https://github.com/KajalGada/leetcode-python/tree/main/leetcode-1-two-sum
+ Given we know incrementing either x or y gives a larger value, you want to increment x if f(x,y) < z and decrement y if f(x,y) > z.
