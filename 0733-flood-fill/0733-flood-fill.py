class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        if not image:
            return [[]]
        
        def vp(row, col, n, m):
            if 0 <= row < n and 0 <= col < m:
                return True
            return False
        
        def dfs(row, col, initial, n, m):
            if not vp(row, col, n, m): return
            if image[row][col] == color: return
            if image[row][col] == initial[0]:
                image[row][col] = color
                
            for i, j in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                if vp(row + i, col + j, n, m) and image[row+i][col+j] in initial:
                    dfs(row+i, col+j, initial, n, m)
        
        initial = (image[sr][sc], color)
        n = len(image)
        m = len(image[sr])
        dfs(sr, sc, initial, n, m)
        
        return image