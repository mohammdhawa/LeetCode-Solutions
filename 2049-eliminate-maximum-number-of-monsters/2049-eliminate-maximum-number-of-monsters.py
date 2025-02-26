class Solution:
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        for i in range(len(dist)):
            dist[i] = dist[i] / speed[i]

        dist.sort()

        for i in range(len(dist)):
            if dist[i] <= i:
                return i
        return len(dist)