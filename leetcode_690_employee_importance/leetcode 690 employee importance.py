"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        emp_dict = {}
        for each_emp in employees:
            emp_dict[each_emp.id] = [each_emp.importance , each_emp.subordinates]
            
        id_list = [id]
        total_imp = 0
        while id_list:
            cur_id = id_list.pop()
            total_imp += emp_dict[cur_id][0]
            id_list += emp_dict[cur_id][1]
            
        return total_imp
