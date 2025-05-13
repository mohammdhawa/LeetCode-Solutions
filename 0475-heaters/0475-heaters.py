class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        def closest_heater(x):
            l, r = 0, len(heaters) - 1
            while l <= r:
                mid = (l + r) // 2
                if heaters[mid] == x:
                    return 0
                if heaters[mid] < x:
                    l = mid + 1
                else:
                    r = mid - 1

            min_dist = float('inf')
            if r >= 0:
                min_dist = min(min_dist, abs(heaters[r] - x))
            if l < len(heaters):
                min_dist = min(min_dist, abs(heaters[l] - x))
            
            return min_dist
        
        # houses.sort()
        heaters.sort()
        result = 0
        for x in houses:
            temp = closest_heater(x)
            result = max(result, temp)
        return result