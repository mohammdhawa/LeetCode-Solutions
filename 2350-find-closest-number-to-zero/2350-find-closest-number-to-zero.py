class Solution:
    def findClosestNumber(self, nums) -> int:
        number, closest_val = nums[0], abs(nums[0] - 0)

        for num in nums[1:]:
            temp = abs(num - 0)
            if closest_val == temp and number < num:
                number = num
                continue
            if temp < closest_val:
                closest_val = temp
                number = num

        return number