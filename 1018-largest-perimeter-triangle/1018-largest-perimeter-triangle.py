class Solution:
    def count_sort(self, arr):
        min_ele = min(arr)
        max_ele = max(arr)
        count = [0 for _ in range(max_ele - min_ele + 1)]

        for x in arr:
            count[x - min_ele] += 1

        idx = 0
        for i in range(len(count)):
            for j in range(count[i]):
                arr[idx] = i + min_ele
                idx += 1

    def largestPerimeter(self, nums: list[int]) -> int:
        self.count_sort(nums)
        def valid(a, b, c):
            if a + b <= c:
                return False
            if a + c <= b:
                return False
            if b + c <= a:
                return False
            return True
        max_perimeter = 0
        for i in range(len(nums) - 2):
            if valid(nums[i], nums[i + 1], nums[i + 2]):
                x = sum(nums[i:i + 3])
                if x > max_perimeter:
                    max_perimeter = x
        return max_perimeter