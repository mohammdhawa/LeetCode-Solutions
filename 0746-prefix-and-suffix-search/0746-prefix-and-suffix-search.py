class WordFilter:

    def __init__(self, words: list[str]):
        self.trie = {}

        for idx, word in enumerate(words):
            for i in range(len(word) + 1):
                curr = self.trie
                suff_word = word[i:]
                key = suff_word + '#' + word
                for ch in key:
                    if ch not in curr:
                        curr[ch] = {}
                    curr = curr[ch]
                    if 'index' not in curr:
                        curr['index'] = [idx]
                    else:
                        curr['index'].append(idx)


    def f(self, pref: str, suff: str) -> int:
        key = suff + '#' + pref
        curr = self.trie
        index = 0
        for ch in key:
            if ch not in curr:
                return -1
            curr = curr[ch]

        return max(curr.get('index', -1))