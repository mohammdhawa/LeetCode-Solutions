class Solution:
    def findSubarrays(self, nums):
        d = {}

        if len(nums) <= 2:
            return False

        for idx in range(len(nums) - 1):
            _sum = nums[idx] + nums[idx + 1]
            if _sum in d:
                d[_sum] += 1
                if d[_sum] == 2:
                    return True
            else:
                d[_sum] = 1

        return any(x == 2 for x in d.values())
        