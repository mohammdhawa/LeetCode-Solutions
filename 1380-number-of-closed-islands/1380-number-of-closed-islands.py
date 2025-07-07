class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [[False for _ in range(m)] for _ in range(n)]

        def dfs(i, j):
            visited[i][j] = True
            flag = True

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                n_i, n_j = dx + i, dy + j
                if not (0 <= n_i < n and 0 <= n_j < m):
                    flag = False
                elif grid[n_i][n_j] == 0 and not visited[n_i][n_j]:
                    flag = dfs(n_i, n_j) and flag

            return flag

        count = 0
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j] == 0:
                    if dfs(i, j):
                        count += 1

        return count