class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        dp = {}
        n, m = len(matrix), len(matrix[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        result = 0

        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]

            best = 1
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] > matrix[i][j]:
                    best = max(best, 1 + dfs(ni, nj))

            dp[(i, j)] = best
            return best


        for row in range(n):
            for col in range(m):
                result = max(result, dfs(row, col))

        return result