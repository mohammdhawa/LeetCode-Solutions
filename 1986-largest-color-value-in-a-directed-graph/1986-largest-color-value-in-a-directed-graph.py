class Solution:
    def largestPathValue(self, colors: str, edges: list[list[int]]) -> int:
        from collections import defaultdict, deque, Counter

        n = len(colors)
        graph = defaultdict(list)
        indegree = [0] * n
        dp = [[0] * 26 for _ in range(n)]
        visited = 0
        answer = 0

        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        queue = deque([i for i in range(n) if indegree[i] == 0])

        for i in range(n):
            dp[i][ord(colors[i]) - ord('a')] = 1

        while queue:
            node = queue.popleft()

            visited += 1

            answer = max(answer, max(dp[node]))

            for neighbor in graph[node]:
                for c in range(26):
                    dp[neighbor][c] = max(dp[neighbor][c], dp[node][c] + (1 if ord(colors[neighbor]) - ord('a') == c else 0))
                
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
            
        return -1 if visited < n else answer