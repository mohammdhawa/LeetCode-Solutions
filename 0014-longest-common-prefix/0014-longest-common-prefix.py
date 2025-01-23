class Solution:
    def __init__(self):
        self.trie = {}

    def _insert(self, word):
        curr = self.trie
        wrd = ""
        for letter in word:
            wrd += letter
            if letter not in curr:
                curr[letter] = {}
            if len(curr) == 1 and letter not in curr:
                return wrd
            curr = curr[letter]


    def longestCommonPrefix(self, strs):
        _min = len(strs[0])
        wrd = strs[0]
        for word in strs:
            if len(word) < _min:
                _min = len(word)
                wrd = word
            self._insert(word)

        curr = self.trie
        result = ""
        for letter in wrd:
            if letter not in curr:
                return result
            if len(curr) > 1:
                return result
            result += letter
            curr = curr[letter]
        return result