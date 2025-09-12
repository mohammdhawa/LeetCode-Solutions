class Solution:
    def maxFreqSum(self, s: str) -> int:
        from collections import defaultdict

        vowel_hash = defaultdict(int)
        consonant_hash = defaultdict(int)

        for ch in s:
            if ch in "aeiou":
                vowel_hash[ch] += 1
            else:
                consonant_hash[ch] += 1

        return max(vowel_hash.values() if vowel_hash else [0]) + max(consonant_hash.values() if consonant_hash else [0])