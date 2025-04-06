class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        l, r = 0, n - 1

        while l < n - 1 and nums[l] <= nums[l + 1]:
            l += 1
        if l == n - 1:
            return 0

        while r > 0 and nums[r] >= nums[r - 1]:
            r -= 1

        min_val = min(nums[l:r+1])
        max_val = max(nums[l:r+1])

        while l > 0 and nums[l-1] > min_val:
            l -= 1
        while r < n - 1 and nums[r + 1] < max_val:
            r += 1
        return r - l + 1