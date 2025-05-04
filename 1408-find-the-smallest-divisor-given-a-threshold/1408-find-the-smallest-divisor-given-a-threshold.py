import math

class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        def f(arr, n):
            _sum = 0
            for x in arr:
                _sum += math.ceil(x / n)
            return _sum

        l, r = 1, max(nums)
        answer = 0
        while l <= r:
            mid = l + (r - l) // 2
            if f(nums, mid) <= threshold:
                answer = mid
                r = mid - 1
            else:
                l = mid + 1
        return answer
