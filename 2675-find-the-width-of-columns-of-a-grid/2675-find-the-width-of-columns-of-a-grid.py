class Solution:
    def findColumnWidth(self, grid: list[list[int]]) -> list[int]:
        return [max(len(str(row[i])) for row in grid) for i in range(len(grid[0]))]