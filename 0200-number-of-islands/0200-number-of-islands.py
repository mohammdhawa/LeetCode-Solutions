class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        def vp(i, j, n, m):
            if 0 <= i < n and 0 <= j < m and grid[i][j] == "1":
                return True
            return False

        def dfs(i, j, n, m):
            if grid[i][j] == "v": return
            grid[i][j] = "v"

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if vp(dx + i, dy + j, n, m):
                    dfs(dx + i, dy + j, n, m)

        n, m =  len(grid), len(grid[0])
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    dfs(i, j, n, m)
                    count += 1
        return count