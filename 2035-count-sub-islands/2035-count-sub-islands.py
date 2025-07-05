class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        def vp(i, j, n, m):
            print(i, j)
            if i < 0 or i >= n:
                return False
            if j < 0 or j >= m:
                return False
            return True

        def dfs(i, j, n, m):
            if not vp(i, j, n, m) or visited[i][j] or grid2[i][j] == 0:
                return True

            visited[i][j] = True

            is_sub = grid1[i][j] == 1

            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                if not dfs(dx + i, dy + j, n, m):
                    is_sub = False

            return is_sub

        n, m =  len(grid2), len(grid2[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        count = 0
        for i in range(n):
            for j in range(m):
                if grid2[i][j] == 1 and not visited[i][j]:
                    if dfs(i, j, n, m):
                        count += 1
        return count