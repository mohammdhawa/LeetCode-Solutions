class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        from collections import deque

        flatten = []
        for i in board:
            for j in i:
                flatten.append(j)

        queue = deque([(flatten, 0)])
        visited = set()
        target = [1, 2, 3, 4, 5, 0]
        neighbors = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }

        if flatten == target:
            return 0

        while queue:
            state, step = queue.popleft()
            visited.add(tuple(state))

            for idx in range(6):
                if state[idx] == 0:
                    for j in neighbors[idx]:
                        temp = state.copy()
                        temp[idx], temp[j] = temp[j], temp[idx]
                        if tuple(temp) not in visited:
                            queue.append((temp, step + 1))
                            if temp == target:
                                return step + 1
        return -1