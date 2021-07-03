Leetcode 463 Island perimeter

Leetcode problem link: https://leetcode.com/problems/island-perimeter/

Solution:
+ Perimeter is all side of occupied cell minus any common sides.
+ You have to subtract common side twice. Thus you have to loop through each cell.


+ Loop through each cell. If it is island, add 4 to perimeter.
+ Check all its neighbours and subtract one for any occupied neighbour. 
