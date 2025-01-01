class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        def prefix(d, word):
            mystr = ''
            for l in word:
                mystr += l
                if d.get(mystr) is not None:
                    return mystr
            return mystr

        d = {}

        for word in dictionary:
            d[word] = True

        mylist = sentence.split()

        for i in range(len(mylist)):
            mylist[i] = prefix(d, mylist[i])

        return ' '.join(mylist)