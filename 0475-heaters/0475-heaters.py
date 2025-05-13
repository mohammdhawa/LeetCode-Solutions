class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        heaters.sort()
        
        def closest_heater(x):
            l, r = 0, len(heaters) - 1
            while l <= r:
                mid = l + (r - l)//2
                if heaters[mid] < x:
                    l = mid + 1
                else:
                    r = mid - 1
            
            dist1 = abs(heaters[l] - x) if l < len(heaters) else float('inf')
            dist2 = abs(heaters[r] - x) if x >= 0 else float('inf')
            return min(dist1, dist2)
        
        return max(closest_heater(x) for x in houses)
