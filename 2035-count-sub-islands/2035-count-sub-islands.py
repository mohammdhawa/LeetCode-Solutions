class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        n, m = len(grid2), len(grid2[0])
        count = 0
        
        def dfs(i, j):
            # Base case: out of bounds or water or already visited
            if i < 0 or i >= n or j < 0 or j >= m or grid2[i][j] == 0:
                return True
            
            # Mark as visited by setting to 0
            grid2[i][j] = 0
            
            # Check if current cell is part of a sub-island
            is_sub = grid1[i][j] == 1
            
            # Explore all 4 directions
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                # If any connected cell is not a sub-island, the whole component isn't
                if not dfs(i + di, j + dj):
                    is_sub = False
            
            return is_sub
        
        # Iterate through all cells in grid2
        for i in range(n):
            for j in range(m):
                if grid2[i][j] == 1:  # Found an unvisited island
                    if dfs(i, j):
                        count += 1
        
        return count