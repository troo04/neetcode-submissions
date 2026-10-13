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
        employee_table = defaultdict(None)

        for e in employees:
            employee_table[e.id] = e
        
        def dfs(employee):
            total = employee.importance

            for sub in employee.subordinates:
                total += dfs(employee_table[sub])
            
            return total

        total = 0
        for employee in employees:
            if employee.id == id:
                total = dfs(employee)
        
        return total