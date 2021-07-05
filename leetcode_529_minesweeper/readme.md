Leetcode 529 Minesweeper

Problem link: https://leetcode.com/problems/minesweeper/

Solution:
+ If click is a mine, mark it X and return
+ Else explore the node and its neighbours.
+ For each node, look at its neighbours and all mines. Keep a tmp list of neighbours that are empty and unrevealed
+ If zero mines, mark it as revealed blank square. Add add its empty unrevealed neighbours for exploration.
+ Else mark the squre with number of mines and its neighbours won't be explored further.

