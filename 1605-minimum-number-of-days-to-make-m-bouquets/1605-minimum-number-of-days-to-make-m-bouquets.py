class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        def check_bouquets_count(n):
            bouquet = 0
            bouquets_count = 0
            for x in bloomDay:
                if x <= n:
                    bouquet += 1
                else:
                    bouquet = 0

                if bouquet == k:
                    bouquets_count += 1
                    bouquet = 0
                if bouquets_count == m:
                    return bouquets_count

            return bouquets_count

        l, r = min(bloomDay), max(bloomDay)
        result = 0
        while l <= r:
            mid = l + (r - l) // 2
            if check_bouquets_count(mid) >= m:
                result = mid
                r = mid - 1
            else:
                l = mid + 1
        return result