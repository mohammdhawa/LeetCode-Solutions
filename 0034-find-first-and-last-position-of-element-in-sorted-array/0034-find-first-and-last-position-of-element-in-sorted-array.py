class Solution:
    def searchRange(self, nums, target):
        def left_target(nums, target):
            l, r, first = 0, len(nums) - 1, -1

            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    first = mid
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return first

        def right_target(nums, target):
            l, r, last = 0, len(nums) - 1, -1

            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    last = mid
                    l = mid + 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return last

        return [left_target(nums, target), right_target(nums, target)]