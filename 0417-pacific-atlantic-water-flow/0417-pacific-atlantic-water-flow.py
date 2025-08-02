class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        n, m = len(heights), len(heights[0])
        pacific_ocean = set()
        atlantic_ocean = set()

        def bfs(i, j, visited):
            queue = [(i, j, heights[i][j])]

            if (i, j) in visited:
                return
            visited.add((i, j))

            while queue:
                row, col, weight = queue.pop(0)

                for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    ni, nj = row + dx, col + dy
                    if not (0 <= ni < n and 0 <= nj < m) or (ni, nj) in visited:
                        continue

                    if weight <= heights[ni][nj]:
                        queue.append((ni, nj, heights[ni][nj]))
                        visited.add((ni, nj))

        for i in range(n):
            bfs(i, 0, pacific_ocean)  # Left column
            bfs(i, m - 1, atlantic_ocean)  # Right column

        for j in range(m):
            bfs(0, j, pacific_ocean)  # Top row
            bfs(n - 1, j, atlantic_ocean)  # Bottom row

        result = []

        for i, j in pacific_ocean:
            if (i, j) in atlantic_ocean:
                result.append((i, j))

        return result