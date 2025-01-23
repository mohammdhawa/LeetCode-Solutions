class Solution:
    def __init__(self):
        self.trie = {}

    def _insert(self, word):
        curr = self.trie
        for letter in word:
            if letter not in curr:
                curr[letter] = {}
            curr = curr[letter]
        curr['#'] = True


    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

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
            if len(curr) != 1 or '#' in curr:
                break
            result += letter
            curr = curr[letter]
        return result