class Solution:
    def findColumnWidth(self, grid: list[list[int]]) -> list[int]:
        n, m = len(grid), len(grid[0])
        answer = [0] * m

        for i in range(m):
            for j in range(n):
                mystr = str(grid[j][i])
                if len(mystr) > answer[i]:
                    answer[i] = len(mystr)

        return answer
