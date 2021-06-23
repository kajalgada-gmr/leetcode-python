Leetcode 56 Merge Intervals

Problem link: https://leetcode.com/problems/merge-intervals/

+ Sort the intervals.
+ Make first interval as current.
+ Now look at the next interval and check if it can be merged with current interval.
+ If yes, then combine them. Take max of end of current and next interval.
+ If no, then the current interval can't be merged with anything else. So add it
          to the merged intervals list.
+ Next interval now becomes current interval to evaluate.
+ Essentially we are looking at each interval until it can be merged with others.
+ Make sure to add the current interval to merged list at end of for loop.
