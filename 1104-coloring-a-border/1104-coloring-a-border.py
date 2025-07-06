class Solution:
    def colorBorder(self, grid: list[list[int]], row: int, col: int, color: int) -> list[list[int]]:
        temp = grid[row][col]
        n, m = len(grid), len(grid[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        border = []

        def vp(i, j):
            return 0 <= i < n and 0 <= j < m

        def dfs(i, j):
            visited[i][j] = True
            is_border = False

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_i, new_j = dx + i, dy + j
                if not vp(new_i, new_j)  or grid[new_i][new_j] != temp:
                    is_border = True
                elif not visited[new_i][new_j]:
                    dfs(new_i, new_j)

            if is_border:
                border.append((i, j))

        dfs(row, col)

        for i, j in border:
            grid[i][j] = color

        return grid