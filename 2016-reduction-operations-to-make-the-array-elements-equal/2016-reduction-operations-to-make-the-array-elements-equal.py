class Solution:
    def reductionOperations(self, nums) -> int:
        n = len(nums)
        if n == 1:
            return 0
        nums.sort()

        j = n - 1
        operations = 0

        while j > 0:
            if nums[j] == nums[0]:
                return operations
            if nums[j] > nums[j - 1]:
                operations += n - j
            j -= 1
        return operations