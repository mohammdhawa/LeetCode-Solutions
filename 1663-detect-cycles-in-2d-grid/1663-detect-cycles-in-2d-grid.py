class Solution:
    def containsCycle(self, grid: list[list[str]]) -> bool:
        n, m = len(grid), len(grid[0])
        visited = [[False for _ in range(m)] for _ in range(n)]

        def is_bound(i, j):
            return 0 <= i < n and 0 <= j < m

        def dfs(i, j, pi, pj):
            visited[i][j] = True

            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                n_i, n_j = dx + i, dy + j
                if is_bound(n_i, n_j) and grid[i][j] == grid[n_i][n_j]:
                    if not visited[n_i][n_j]:
                        if dfs(n_i, n_j, i, j):
                            return True
                    elif (n_i, n_j) != (pi, pj):
                        return True
            return False

        for i in range(n):
            for j in range(m):
                if not visited[i][j]:
                    if dfs(i, j, -1, -1):
                        return True
        return False