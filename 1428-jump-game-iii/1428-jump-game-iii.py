class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        if not arr:
            return False

        queue = [start]
        n = len(arr)

        while queue:
            index = queue.pop(0)
            if arr[index] == 0:
                return True
            if arr[index] == '#':
                continue

            if 0 <= index - arr[index] < n:
                queue.append(index - arr[index])
            if index + arr[index] < n:
                queue.append(index + arr[index])

            arr[index] = '#'

        return False
