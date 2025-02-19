class Solution:
    def sortArray(self, nums):
        SHIFT = 50000
        for i in range(len(nums)):
            nums[i] = nums[i] + SHIFT

        max_element = max(nums)
        min_element = min(nums)
        count = [0 for _ in range(max_element + 1)]

        for x in nums:
            count[x] += 1

        idx = 0
        for i in range(min_element, len(count)):
            for j in range(count[i]):
                nums[idx] = i - SHIFT
                idx += 1

        return nums