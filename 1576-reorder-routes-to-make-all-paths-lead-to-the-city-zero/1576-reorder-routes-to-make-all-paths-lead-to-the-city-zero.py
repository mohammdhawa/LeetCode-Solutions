class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        from collections import defaultdict
        graph = {i: [] for i in range(n)}
        visited = [False for _ in range(n)]
        count = 0

        for _from, _to in connections:
            graph[_from].append((_to, 0))
            graph[_to].append((_from, 1))

        def dfs(node):
            nonlocal count
            visited[node] = True

            for neighbor, flag in graph[node]:
                if visited[neighbor]: continue
                if flag:
                    dfs(neighbor)
                else:
                    count += 1
                    dfs(neighbor)

        dfs(0)

        return count