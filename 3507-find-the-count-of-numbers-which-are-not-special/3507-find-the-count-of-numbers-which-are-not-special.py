class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        import math

        def is_prime(num):
            if num <= 1:
                return False
            elif num == 2:
                return True
            elif num % 2 == 0:
                return False
            for i in range(3, int(num ** 0.5) + 1, 2):
                if num % i == 0:
                    return False
            return True

        myst = set()
        low, high = math.isqrt(l), math.isqrt(r) + 1

        for i in range(low, high + 1):
            if is_prime(i):
                square = i ** 2
                if square > r:
                    break
                myst.add(square)

        count = sum(1 for i in myst if l <= i <= r)
        return (r - l + 1) - count
