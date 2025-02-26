class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        while k:
            min_ele = min(nums)
            idx = nums.index(min_ele)
            nums[idx] = -min_ele
            k -= 1
        return sum(nums)
        