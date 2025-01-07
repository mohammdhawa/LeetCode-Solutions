class Trie:
    def __init__(self):
        self.child = {}
        self.is_end = False


class MagicDictionary:

    def __init__(self):
        self.root = Trie()

    def _insert(self, word):
        curr = self.root
        for l in word:
            if l not in curr.child:
                curr.child[l] = Trie()
            curr = curr.child[l]
        curr.is_end = True

    def buildDict(self, dictionary: list[str]) -> None:
        for word in dictionary:
            self._insert(word)

    def _search(self, word, index, count, trie):
        if index == len(word):
            return count == 1 and trie.is_end

        char = word[index]
        for key in trie.child:
            if key == char:
                if self._search(word, index + 1, count, trie.child[key]):
                    return True
            else:
                if self._search(word, index + 1, count + 1, trie.child[key]):
                    return True
        return False


    def search(self, searchWord: str) -> bool:
        return self._search(searchWord, 0, 0, self.root)