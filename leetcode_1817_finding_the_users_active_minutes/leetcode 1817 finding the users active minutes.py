class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        
        user_to_time = defaultdict(set)
        for id, time in logs:
            user_to_time[id].add(time)
        uam = [0] * k    
        for times in user_to_time.values():
            uam[len(times) - 1] += 1
        return uam
        
