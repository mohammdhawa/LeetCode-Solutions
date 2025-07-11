class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        keys = set()
        for num in nums:
            keys.add(num)

        max_count = 0
        for num in keys:
            count = 0
            if num - 1 not in keys:
                temp = num + 1
                count = 1
                while temp in keys:
                    count += 1
                    temp += 1

            max_count = max([max_count, count])
        return max_count