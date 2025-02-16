class Solution:
    def sortArray(self, nums):
        min_ele = min(nums)
        max_ele = max(nums)
        if abs(min_ele) > abs(max_ele):
            arr1 = [0 for i in range(abs(min_ele) + 1)]
            arr2 = [0 for i in range(abs(min_ele) + 1)]
        else:
            arr1 = [0 for i in range(max_ele + 1)]
            arr2 = [0 for i in range(max_ele + 1)]

        for x in nums:
            if x < 0:
                arr2[-x] += 1
            else:
                arr1[x] += 1

        i = 0
        for idx in range(len(arr2)-1, -1, -1):
            for j in range(arr2[idx]):
                nums[i] = -idx
                i += 1

        for idx in range(len(arr1)):
            for j in range(arr1[idx]):
                nums[i] = idx
                i += 1
        return nums