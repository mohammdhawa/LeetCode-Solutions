class Solution:
    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        from collections import defaultdict, deque

        graph = defaultdict(list)
        in_degree = [0] * n
        queue = deque()
        finish_time = [0] * n

        for _from, _to in relations:
            graph[_from-1].append(_to-1)
            in_degree[_to-1] += 1

        for i in range(n):
            if in_degree[i] == 0:
                finish_time[i] = time[i]
                queue.append(i)

        while queue:
            node = queue.popleft()

            for neighbor in graph[node]:
                finish_time[neighbor] = max(finish_time[neighbor], finish_time[node] + time[neighbor])

                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return max(finish_time)
