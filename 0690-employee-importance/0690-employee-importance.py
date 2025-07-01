"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: list['Employee'], id: int) -> int:
        n = len(employees)
        visited = [False] * n
        result = 0
        d = {}
        index = -1
        for idx, emp in enumerate(employees):
            d[emp.id] = idx
            if emp.id == id:
                index = idx

        def dfs(node):
            nonlocal result

            if visited[node]: return
            visited[node] = True
            emp = employees[node]
            result += emp.importance

            for neighbor in emp.subordinates:
                dfs(d[neighbor])

        dfs(index)
        return result