class Solution:
    def maxCandies(self, status: list[int], candies: list[int], keys: list[list[int]], containedBoxes: list[list[int]], initialBoxes: list[int]) -> int:
        from collections import deque

        visited = set()
        k = set()
        queue = deque(initialBoxes)
        queue2 = deque()
        result = 0

        while queue:
            state = queue.popleft()

            if state in visited:
                continue

            if status[state] or state in k:
                visited.add(state)
                result += candies[state]
                for x in keys[state]:
                    k.add(x)
                for ele in containedBoxes[state]:
                    queue.append(ele)
                while queue2:
                    queue.append(queue2.popleft())
            else:
                queue2.append(state)

        return result