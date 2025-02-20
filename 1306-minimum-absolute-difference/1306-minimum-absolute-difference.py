class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()
        min_diff = float('inf')

        for i in range(len(arr)-1):
            diff = abs(arr[i] - arr[i+1])
            if diff < min_diff:
                min_diff = diff

        result = []
        for i in range(len(arr)-1):
            diff = abs(arr[i] - arr[i+1])
            if diff == min_diff:
                result.append([arr[i], arr[i+1]])

        return result