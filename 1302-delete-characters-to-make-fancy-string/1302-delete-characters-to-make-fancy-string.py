class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s

        result = ''

        for ch in s:
            if len(result) >= 2 and result[-1] == result[-2] == ch:
                continue
            result += ch

        return result