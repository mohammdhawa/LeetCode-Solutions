class WordFilter:

    def __init__(self, words: list[str]):
        self.dictionary = {}

        for idx, word in enumerate(words):
            for i in range(len(word) + 1):
                suff = word[i:]
                for i in range(len(word) + 1):
                    pref = word[:i]
                    key = f"{suff}#{pref}"
                    if key not in self.dictionary:
                        self.dictionary[key] = [idx]
                    else:
                        self.dictionary[key].append(idx)

    def f(self, pref: str, suff: str) -> int:
        return max(self.dictionary.get(suff + '#' + pref, [-1]))

