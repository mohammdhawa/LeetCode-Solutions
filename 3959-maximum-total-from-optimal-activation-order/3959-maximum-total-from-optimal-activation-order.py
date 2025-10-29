class Solution:
    def maxTotal(self, value: List[int], limit: List[int]) -> int:
        d = defaultdict(list)
        for v,l in zip(value,limit):
            heappush(d[l],v)
            if len(d[l]) > l:
                heappop(d[l])
        return sum(map(sum,d.values()))