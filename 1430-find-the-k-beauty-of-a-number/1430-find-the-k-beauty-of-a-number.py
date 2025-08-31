class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = str(num)
        n = len(num_str)
        count = 0

        for i in range(n):
            x = ''
            if k + i <= n:
                x = num_str[i: i + k]

                if int(x) != 0 and num % int(x) == 0:
                    count += 1
        return count
