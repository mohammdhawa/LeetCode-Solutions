class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        mid = n // 2

        i, j = 0, mid

        result = 0

        while i < mid or j < n:
            if i < mid:
                if n % (i + 1) == 0:
                    result += (nums[i] ** 2)

                i += 1

            if j < n:
                if n % (j + 1) == 0:
                    result += (nums[j] ** 2)

                j += 1

        return result