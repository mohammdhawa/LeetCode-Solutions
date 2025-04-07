class Solution:
    def reductionOperations(self, nums) -> int:
        n = len(nums)
        if n == 1:
            return 0
        nums.sort()

        j = n - 1
        operations = 0
        min_ele = nums[0]

        # while j > 0:
        #     if nums[j] == min_ele:
        #         return operations
        #     if nums[j] > nums[j - 1]:
        #         operations += n - j
        #     j -= 1
        prev = 0
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                prev += 1
            operations += prev
        return operations