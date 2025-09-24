class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []

        def bs(arr: List[int], target: int) -> int:
            l, r = 0, len(arr) - 1

            while l <= r:
                m = (l + r) // 2
                if arr[m] == target:
                    return m
                elif arr[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return l

        for num in nums:
            if not dp or num > dp[-1]:
                dp.append(num)
                continue

            temp = bs(dp, num)
            dp[temp] = num

        return len(dp)
        