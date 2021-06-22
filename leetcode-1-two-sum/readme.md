Leetcode problem 1 Two Sum

Problem link: https://leetcode.com/problems/two-sum/

Solution #1

+ Sort the list of numbers.
+ Have one index at start of the list and another at end of list
+ Compute sum. If it is higher than target, means we need a smaller number so decrement end index.
+ Similarly if the sum of start and end index number is lower than target, we need a higher number. Increment the start index to point to a higher number.

+ Next look for the number in original numbers list (which was unsorted).
+ Remember to look for duplicates.

+ How to search and get index of number in a list?
  + list_name.index(number_to_search)
  + list_name.index(number_to_search, index_num+1) -> to start search from specific index number.


Solution #2

+ Using dictionary
+ Iterate through each number in the list and we will store them in a dictionary.
+ For each number encountered, compute the second number required (target - current_number).
+ Check if that number exists in dictionary. If yes we found both numbers.
+ Else add it to the dictionary. 
+ Dictionary contains key as number and value as index.

