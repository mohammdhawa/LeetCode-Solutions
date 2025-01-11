class WordFilter:

    def __init__(self, words: list[str]):
        self.dictionary = {}

        for idx, word in enumerate(words):
            for i in range(len(word) + 1):
                suff = word[i:]
                if suff not in self.dictionary:
                    self.dictionary[suff] = {'words': [word], 'index': [idx]}
                else:
                    self.dictionary[suff]['words'].append(word)
                    self.dictionary[suff]['index'].append(idx)

    def f(self, pref: str, suff: str) -> int:
        if suff not in self.dictionary:
            return -1
        
        words = self.dictionary[suff]['words'][::-1]
        index = self.dictionary[suff]['index'][::-1]
        for idx, word in enumerate(words):
            if word.startswith(pref):
                return index[idx]
        return -1