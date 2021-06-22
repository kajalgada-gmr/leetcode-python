Leetcode 15 3sum

Problem link: https://leetcode.com/problems/3sum/

Solution:
+ Sort the list cause you only care about numbers and not index.
+ Make 1st number as target and then look through rest of solution for 2nd and 3rd number using 2 sum method.
+ Skip through repeat numbers when incrementing target_ind, left_ind and right_ind.
+ Don't look at postive target number (do look at 0), cause you will never get 0 sum with all positive numbers.
