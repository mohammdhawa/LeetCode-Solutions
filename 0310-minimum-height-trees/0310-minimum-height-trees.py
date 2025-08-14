class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n == 1:
            return [0]

        from collections import deque

        # Build graph and degree array
        graph = {i: [] for i in range(n)}
        degree = [0] * n
        for _from, _to in edges:
            graph[_from].append(_to)
            graph[_to].append(_from)
            degree[_from] += 1
            degree[_to] += 1

        # Initialize leaves
        queue = deque()
        for node in range(n):
            if degree[node] == 1:
                queue.append(node)

        remaining_nodes = n
        # Trim leaves layer by layer
        while remaining_nodes > 2:
            leaf_count = len(queue)
            remaining_nodes -= leaf_count

            for _ in range(leaf_count):
                leaf = queue.popleft()

                for neighbor in graph[leaf]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        queue.append(neighbor)

        return list(queue)