class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: list[list[int]]) -> str:
        if not pairs:
            return s

        n = len(s)
        graph = [[] for _ in range(n)]
        visited = [False] * n
        str_list = list(s)

        for x, y in pairs:
            graph[x].append(y)
            graph[y].append(x)

        def dfs(node, component):
            visited[node] = True
            component.append(node)

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor, component)

        for i, j in enumerate(graph):
            if j and not visited[i]:
                component = []
                dfs(i, component)
                sub_text = ''
                for idx in component:
                    sub_text += str_list[idx]
                sub_text = ''.join(sorted(sub_text))
                component.sort()

                for i, idx in zip(sub_text, component):
                    str_list[idx] = i


        return ''.join(str_list)