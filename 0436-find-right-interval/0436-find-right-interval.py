class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        start_list = [(intervals[i][0], i) for i in range(len(intervals))]
        start_list = sorted(start_list, key=lambda x: x[0])

        def bs(arr, target):
            l, r = 0, len(arr) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if arr[mid][0] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return arr[l][1] if l < len(arr) else -1

        result = []
        for i in range(len(intervals)):
            result.append(bs(start_list, intervals[i][1]))

        return result