class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
        from collections import deque, defaultdict

        red_graph = defaultdict(list)
        blue_graph = defaultdict(list)

        for _from, _to in redEdges:
            red_graph[_from].append(_to)
        for _from, _to in blueEdges:
            blue_graph[_from].append(_to)

        queue = deque([(0, 0, -1)])
        answer = [-1] * n
        visited = set([(0, -1)])

        while queue:
            node, steps, last_color = queue.popleft()

            if answer[node] == -1:
                answer[node] = steps

            if last_color != 0: # if it is not red
                for neighbor in red_graph[node]:
                    if (neighbor, 0) not in visited:
                        visited.add((neighbor, 0))
                        queue.append((neighbor, steps + 1, 0))

            if last_color != 1: # if it is not blue
                for neighbor in blue_graph[node]:
                    if (neighbor, 1) not in visited:
                        visited.add((neighbor, 1))
                        queue.append((neighbor, steps + 1, 1))

        return answer