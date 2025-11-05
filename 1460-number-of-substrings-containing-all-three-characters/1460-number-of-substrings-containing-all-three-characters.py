class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        last = {'a': -1, 'b': -1, 'c' : -1}

        for i, ch in enumerate(s):
            last[ch] = i
            if -1 not in last.values():
                count += 1 + min(last.values())

        return count