class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def bst(nums):
            n = len(nums)
            l = 0
            h = n - 1
            m = n - 1

            while l <= h:
                m = (l + h) // 2
                if nums[m] < 0:
                    h = m - 1
                else:
                    l = m + 1

            if nums[m] < 0:
                return n - m
            return n - m - 1

        count = 0
        for nums in grid:
            count += bst(nums)

        return count