class Solution:
    def opt(self, x, m, n):
        count = 0
        for row in range(1, m + 1):
            count += min(x // row, n)
        return count

    def findKthNumber(self, m: int, n: int, k: int) -> int:
        l, r = 1, n * m
        
        while l < r:
            mid = l + (r - l) // 2
            if self.opt(mid, m, n) < k:
                l = mid + 1
            else:
                r = mid
        return l