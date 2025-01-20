class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        mylist = list(s)
        mystr = ""
        j = 0

        for idx in spaces:
            mystr += ''.join(mylist[j:idx]) + ' '
            j = idx
        mystr += ''.join(mylist[j:])
        return mystr