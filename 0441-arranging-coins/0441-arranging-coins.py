class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1
        l, r = 0, n - 1
        result = []
        
        while l <= r:
            mid = l + (r - l) // 2
            if mid * (mid + 1) // 2 <= n:
                if result and result[-1] < mid:
                    result.append(mid)
                else:
                    result.append(mid)
                l = mid + 1
            else:
                r = mid - 1
        return result[-1]