class Solution:
    def minimumOperations(self, nums: list[int], start: int, goal: int) -> int:
        visited = set()
        queue = [(start, 0)]

        while queue:
            x, step = queue.pop(0)

            if x == goal:
                return step

            if x < 0 or x > 1000:
                continue

            if x in visited:
                continue
            visited.add(x)

            for num in nums:
                for op in (x + num, x - num, x ^ num):
                    if op == goal:
                        return step + 1
                    if 0 <= op <= 1000 and op not in visited:
                        queue.append((op, step + 1))
        return -1