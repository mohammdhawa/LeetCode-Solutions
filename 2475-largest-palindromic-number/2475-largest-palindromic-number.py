class Solution:
    def largestPalindromic(self, num: str) -> str:
        from collections import Counter

        num_map = Counter(num)
        sorted_nums = sorted(set(num), reverse=True)
        flag = -1
        result = []

        for x in sorted_nums:
            if not result and x == '0':
                continue
            if num_map[x] % 2 == 1:
                if flag == -1:
                    flag = x
                for i in range(num_map[x] // 2):
                    result.append(x)
            else:
                for i in range(num_map[x] // 2):
                    result.append(x)

        answer = ''
        if flag != -1:
            answer = ''.join(result) + str(flag) + ''.join(reversed(result))
        else:
            answer = ''.join(result) + ''.join(reversed(result))

        return "0" if answer == '' else answer