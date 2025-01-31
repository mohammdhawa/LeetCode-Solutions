class Solution:
    def smallestNumber(self, n: int) -> int:
        def bin_num(n):
            s = 0
            while n:
                s += 1
                n //= 2
            return s

        return int('1' * bin_num(n), 2)
