Leetcode 1817. Finding the Users Active Minutes

Problem link: https://leetcode.com/problems/finding-the-users-active-minutes/

Solution:
+ We want to track all the users log in history and only save the unique times. So we make use of defaultdict(set).
+ Set helps store unique values.
+ Dict (hashmap) allows to quickly save information about each user.
+ We loop through all the user id and time.
+ Next we loop through all saved user id info and count amount of active minutes. We add this count to list of active users for a given active minute usage.

LEARNING: defaultdict(set) (from collections import defauldict)
