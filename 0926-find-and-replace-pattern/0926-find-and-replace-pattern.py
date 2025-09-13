class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        from collections import defaultdict

        result = []
        pattern_map = defaultdict(int)

        for idx, ch in enumerate(pattern):
            pattern_map[ch] += (idx * 10) + 1

        for word in words:
            word_map = defaultdict(int)

            for idx, ch in enumerate(word):
                word_map[ch] += (idx * 10) + 1

            if tuple(word_map.values()) == tuple(pattern_map.values()):
                result.append(word)

        return result