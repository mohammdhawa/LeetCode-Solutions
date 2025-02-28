class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        temp = nums.copy()
        left = -1
        right = -1
        nums.sort()
        for i in range(len(nums)):
            if temp[i] != nums[i]:
                if left == -1 and right == -1:
                    left = right = i
                else:
                    right = i
        if left == -1:
            return 0
        return right - left + 1