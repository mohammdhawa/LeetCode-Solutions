class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        deadends = set(deadends)
        visited = set()

        if '0000' in deadends:
            return -1
        def get_neighbors(state: str) -> list[str]:
            neighbors = []
            for i in range(4):
                digit = int(state[i])
                # Turn the wheel one step forward
                up = (digit + 1) % 10
                # Turn the wheel one step backward
                down = (digit - 1) % 10

                neighbors.append(state[:i] + str(up) + state[i + 1:])
                neighbors.append(state[:i] + str(down) + state[i + 1:])

            return neighbors

        queue = [('0000', 0)]
        visited.add('0000')

        while queue:
            node, path = queue.pop(0)
            if node == target:
                return path

            for neighbor in get_neighbors(node):
                if neighbor not in deadends and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + 1))

        return -1