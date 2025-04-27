class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n - 1
        result = 1
        
        while l <= r:
            mid = l + (r - l) // 2
            if mid * (mid + 1) // 2 <= n:
                if result < mid:
                    result = mid
                l = mid + 1
            else:
                r = mid - 1
        return result