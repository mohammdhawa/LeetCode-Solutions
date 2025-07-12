class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        color = {}

        def dfs(node, c):
            if node in color:
                return color[node] == c

            color[node] = c

            for neighbor in graph[node]:
                if not dfs(neighbor, 1 - c):
                    return False
            return True

        for v in range(len(graph)):
            if v not in color:
                if not dfs(v, 1):
                    return False
        return True