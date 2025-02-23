class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        def valid(a, b, c):
            if a + b <= c:
                return False
            if a + c <= b:
                return False
            if b + c <= a:
                return False
            return True
        nums.sort(reverse=True)
        max_perimeter = 0
        for i in range(len(nums) - 2):
            if valid(nums[i], nums[i + 1], nums[i + 2]):
                x = sum(nums[i:i + 3])
                if x > max_perimeter:
                    max_perimeter = x
        return max_perimeter