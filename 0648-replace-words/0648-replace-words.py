class Trie:
    def __init__(self):
        self.child = [None] * 26
        self.is_end = False

    def letter_index(self, letter):
        return ord(letter) - ord('a')

    def insert(self, str):
        curr = self

        for letter in str:
            letter_index = self.letter_index(letter)
            if curr.child[letter_index] is None:
                curr.child[letter_index] = Trie()
            curr = curr.child[letter_index]

        curr.is_end = True

    def prefix(self, prefix):
        if self.child[self.letter_index(prefix[0])] is None:
            return False, ''
        curr = self
        word = ''

        for l in prefix:
            l_idx = self.letter_index(l)
            if curr.child[l_idx] is None:
                break
            word += chr(l_idx + ord('a'))
            if curr.child[l_idx].is_end:
                return True, word
            curr = curr.child[l_idx]

        return (True, word) if curr.is_end else (False, '')


class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        mylist = sentence.split()
        trie = Trie()

        for root in dictionary:
            trie.insert(root)

        for idx in range(len(mylist)):
            flag, word = trie.prefix(mylist[idx])
            if flag:
                mylist[idx] = word

        return ' '.join(mylist)