class Solution:
    def digitCount(self, num: str) -> bool:
        d = {}
        for x in num:
            if d.get(x) is None:
                d[x] = 1
            else:
                d[x] += 1

        for idx in range(len(num)):
            if d.get(str(idx), 0) == 0:
                if int(num[idx]) == 0:
                    continue
            if int(num[idx]) != d.get(str(idx)):
                return False
        return True