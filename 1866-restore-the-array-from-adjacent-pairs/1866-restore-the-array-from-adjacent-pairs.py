class Solution:
    def restoreArray(self, adjacentPairs: list[list[int]]) -> list[int]:
        from collections import defaultdict

        graph = defaultdict(list)
        for x, y in adjacentPairs:
            graph[x].append(y)
            graph[y].append(x)

        start = None
        for node in graph:
            if len(graph[node]) == 1:
                start = node
                break

        visited = set()
        result = []

        def dfs(node):
            visited.add(node)
            result.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(start)
        return result