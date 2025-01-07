class MagicDictionary:

    def __init__(self):
        from collections import defaultdict
        self.patterns_dict = defaultdict(list)

    def buildDict(self, dictionary: list[str]) -> None:
        for word in dictionary:
            for i in range(len(word)):
                word_pattern = word[:i] + '*' + word[i+1:]
                self.patterns_dict[word_pattern].append(word)

    def search(self, searchWord: str) -> bool:
        for i in range(len(searchWord)):
            word_pattern = searchWord[:i] + '*' + searchWord[i+1:]
            if word_pattern in self.patterns_dict:
                for word in self.patterns_dict[word_pattern]:
                    if word != searchWord:
                        return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)