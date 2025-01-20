class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        mystr = ""
        j = 0

        for idx in spaces:
            mystr += s[j:idx] + ' '
            j = idx
        mystr += s[j:]
        return mystr