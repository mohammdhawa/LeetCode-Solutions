class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        visited = [
            [False for _ in range(cols)] for _ in range(rows)
        ]

        def reset_visited():
            for row in range(rows):
                for col in range(cols):
                    visited[row][col] = False

        def valid_position(i, j):
            return 0 <= i < rows and 0 <= j < cols

        def dfs(i, j, h):
            visited[i][j] = True
            if i == rows - 1 and j == cols - 1:
                return

            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                n_i, n_j = i + dx, j + dy
                if not valid_position(n_i, n_j) or visited[n_i][n_j]: continue

                path = abs(heights[n_i][n_j] - heights[i][j])
                if path <= h:
                    dfs(n_i, n_j, h)

        l, r = 0, 10**6
        result = r

        while l <= r:
            reset_visited()
            mid = l + (r - l) // 2

            dfs(0, 0, mid)
            if visited[-1][-1]:
                r = mid - 1
                if result > mid:
                    result = mid
            else:
                l = mid + 1


        return result

