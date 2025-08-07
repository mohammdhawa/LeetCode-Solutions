class Solution:
    def maxCandies(self, status: list[int], candies: list[int], keys: list[list[int]], containedBoxes: list[list[int]], initialBoxes: list[int]) -> int:
        from collections import deque

        visited = [False] * len(status)
        k = [False] * len(status)
        queue = deque(initialBoxes)
        queue2 = deque()
        result = 0

        while queue:
            state = queue.popleft()

            if visited[state]:
                continue

            if status[state] or k[state]:
                visited[state] = True
                result += candies[state]
                for idx in keys[state]:
                    k[idx] = True
                for ele in containedBoxes[state]:
                    queue.append(ele)
                while queue2:
                    queue.append(queue2.popleft())
            else:
                queue2.append(state)

        return result