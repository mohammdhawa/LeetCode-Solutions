class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        pair_sum = 0
        for i in range(0, len(nums), 2):
            pair_sum += nums[i]
        return pair_sum
