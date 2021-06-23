Leetcode 62 unique Paths

Problem link: https://leetcode.com/problems/unique-paths/

Solution 1:
+ Robot can go right or down.
+ So look at each cube and think of how many ways it can reach there.
+ For row 0, it can only go right so all locations in row 0 there is only 1 way to reach there.
+ Similarly, for col 0, only one way.
+ Now 1,1: 2 ways: right down or down right. In other words 2 ways. 
+ Both of those ways is from top and left. In other words you can reach 1,1 from 0,1 and 1,0
+ So number of ways to reach 1,1 = num of ways to reach 0,1 and num of ways to reach 1,0
+ General formula: n,n = m-1,n + m,n-1

+ For python, create matrix with np.ones((m,n), dtype=int)

