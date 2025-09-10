class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        _sum = 0
        flag = False
        cost.sort(reverse=True)

        i = 0
        while i < len(cost):
            if flag:
                flag = not flag
                i += 1
                continue

            flag = not flag
            _sum += cost[i]
            if i + 1 < len(cost): _sum += cost[i + 1]
            i += 2

        return _sum