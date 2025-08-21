class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        hash_set = set(nums)
        max_element = -1

        for num in hash_set:
            if num > max_element and -num in hash_set:
                max_element = num
        return max_element