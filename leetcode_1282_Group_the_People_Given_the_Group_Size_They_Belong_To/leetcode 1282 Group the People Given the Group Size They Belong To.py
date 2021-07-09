class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        final_groups = []
        group_size_dict = {}
        
        for person_id, group_size in enumerate(groupSizes):
            
            if group_size == 1:
                final_groups.append([person_id])
                
            elif group_size in group_size_dict:
                
                group_size_dict[group_size] += [person_id]
                
                if len(group_size_dict[group_size]) == group_size:
                    final_groups.append(group_size_dict[group_size])
                    del group_size_dict[group_size]
                    
            else:
                group_size_dict[group_size] = [person_id]
        
        return final_groups
        
