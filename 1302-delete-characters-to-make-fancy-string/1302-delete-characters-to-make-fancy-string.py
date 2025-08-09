class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s

        prev = s[0]
        count = 1
        i = 1
        result = prev

        while i < len(s):
            if prev == s[i]:
                count += 1
            else:
                prev = s[i]
                count = 1

            i += 1

            if count > 2:
                continue
            else:
                result += prev

        return result