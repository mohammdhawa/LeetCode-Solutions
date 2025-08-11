class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        if not prerequisites:
            return True

        from collections import deque

        graph = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses

        for _to, _from in prerequisites:
            graph[_from].append(_to)
            in_degree[_to] += 1

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        count = 0

        while queue:
            node = queue.popleft()

            count += 1

            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return count == numCourses