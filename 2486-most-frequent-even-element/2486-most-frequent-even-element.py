class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        from collections import Counter

        d_counter = {}
        for num in nums:
            if num % 2 == 0:
                if num in d_counter:
                    d_counter[num] += 1
                else:
                    d_counter[num] = 1
        count = -1
        _key = -1
        for key, val in d_counter.items():
            if val > count:
                count = val
                _key = key
            elif val == count:
                _key = key if key < _key else _key

        return _key