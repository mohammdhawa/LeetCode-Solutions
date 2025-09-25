class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)

        if sum_nums % 2 == 1:
            return False

        dp = [False] * (sum_nums // 2 + 1)
        dp[0] = True

        for num in nums:
            for t in range(sum_nums // 2, num - 1, -1):
                dp[t] = dp[t] or dp[t - num]

        return dp[sum_nums // 2]