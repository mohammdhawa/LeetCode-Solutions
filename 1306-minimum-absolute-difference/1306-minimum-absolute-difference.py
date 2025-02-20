class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()
        min_diff = float('inf')
        d = {}
        for i in range(len(arr)-1):
            diff = abs(arr[i] - arr[i+1])
            if d.get(diff):
                d[diff].append([arr[i], arr[i+1]])
            else:
                d[diff] = []
                d[diff].append([arr[i], arr[i+1]])
            if diff < min_diff:
                min_diff = diff

        return d.get(min_diff)