class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums_set = set(nums)

        if len(nums_set) == 1:
            for num in nums_set:
                if num == k:
                    return 0
                elif num < k:
                    return -1
            return 1

        if min(nums_set) > k:
            return len(nums_set)
        if min(nums_set) < k:
            return -1
        if max(nums_set) <= k:
            return -1

        count = 0
        for num in nums_set:
            if num > k:
                count += 1
        return count