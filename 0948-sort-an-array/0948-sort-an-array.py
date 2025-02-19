class Solution:
    def sortArray(self, nums):
        min_element = min(nums)
        max_element = max(nums)
        max2 = max_element - min_element + 1
        count = [0 for _ in range(max2)]

        for x in nums:
            count[x - min_element] += 1

        idx = 0
        for i in range(max2):
            for j in range(count[i]):
                nums[idx] = i + min_element
                idx += 1
        return nums