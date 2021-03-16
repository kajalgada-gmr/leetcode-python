Leetcode Split Linkedin List in Parts

Leetcode problem 725: https://leetcode.com/problems/split-linked-list-in-parts/

Learnings:

- Read question properly. You have to divide the list into part. So you have to add each node to each part and remember to put last part of each node as none.
- Tricky part is computing each of the part size and index.
- So compute number of parts which will have extra number → large parts.
- And small parts = total parts (k) - large parts
- Then simply loop through (len_ of_part + 1) for large parts and len_of_part for small parts.

Tags: Leetcode, Leetcode python, Leetcode 725, Leetcode 725 python, Leetcode split linked list in parts, leetcode split linked list in parts python solution, leetcode python solution, leetcode 725 python solution
