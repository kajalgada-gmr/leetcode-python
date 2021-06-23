class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # Sort intervals. They will be done based on 1st element of each interval
        intervals.sort()
        merged_intervals = []
        
        cur_interval = intervals.pop(0)
        
        # Iterate through each interval
        for next_interval in intervals:
            
            # Check if the next interval can be combined
            # Don't add it to merge list yet cause the next next interval
            #  might also get combined.
            if cur_interval[1] >= next_interval[0]:
                cur_interval[1] = max(cur_interval[1], next_interval[1])
                
            # Since the interval can't be merges, add it to merge list.
            else:
                merged_intervals.append(cur_interval)
                cur_interval = next_interval[:]  # to ensure copy and not pointer!
                
        merged_intervals.append(cur_interval)
                
        return merged_intervals
        
