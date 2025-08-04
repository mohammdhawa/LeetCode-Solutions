class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target == 0 or target == x + y:
            return True

        from collections import deque

        queue = deque()
        queue.append((0, 0))
        visited = set()

        def pour(from_amt, from_cap, to_amt, to_cap):
            pour_amt = min(from_amt, to_cap - to_amt)
            new_from_amt = from_amt - pour_amt
            new_to_amt = to_amt + pour_amt
            return new_from_amt, new_to_amt

        while queue:
            j1, j2 = queue.popleft()

            if j1 + j2 == target:
                return True

            visited.add((j1, j2))

            i1, j1_ = pour(j1, x, j2, y)
            i2, j2_ = pour(j2, y, j1, x)
            for i, j in [(0, j2), (x, j2), (j1, 0), (j1, y), (i1, j1_), (j2_, i2)]:
                if (i, j) not in visited:
                    queue.append((i, j))

        return False

s = Solution()
print(s.canMeasureWater(1, 2, 3))

