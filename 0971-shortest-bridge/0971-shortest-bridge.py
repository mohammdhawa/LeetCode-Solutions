class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        from collections import deque

        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()

        def dfs(i, j):
            if not (0 <= i < n and 0 <= j < n) or visited[i][j] or grid[i][j] != 1:
                return
            visited[i][j] = True
            queue.append((i, j))
            for dx, dy in directions:
                dfs(i + dx, j + dy)

        # Find and mark the first island
        found = False
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break
            if found:
                break

        # BFS to expand to second island
        steps = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                        if grid[ni][nj] == 1:
                            return steps
                        visited[ni][nj] = True
                        queue.append((ni, nj))
            steps += 1

        return steps
