class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        from collections import defaultdict

        def check(nums1, nums2):
            if len(nums1) != len(nums2):
                return False
            for x, y in zip(nums1, nums2):
                if x != y:
                    return False

            return True

        result = []
        pattern_map = defaultdict(int)

        for idx, ch in enumerate(pattern):
            pattern_map[ch] += (idx * 10) + 1

        for word in words:
            word_map = defaultdict(int)

            for idx, ch in enumerate(word):
                word_map[ch] += (idx * 10) + 1

            if check(word_map.values(), pattern_map.values()):
                result.append(word)

        return result