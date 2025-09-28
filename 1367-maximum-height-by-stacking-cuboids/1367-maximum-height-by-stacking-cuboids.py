class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        for cuboid in cuboids:
            cuboid.sort()
        cuboids.sort()

        def compare_cuboids(c1: List[int], c2: List[int]) -> bool:
            if c1[0] <= c2[0] and c1[1] <= c2[1] and c1[2] <= c2[2]:
                return True
            return False

        n = len(cuboids)
        dp = [0] * n

        for i in range(n):
            dp[i] = cuboids[i][2]
            for j in range(i):
                if compare_cuboids(cuboids[j], cuboids[i]):
                    print(f"dp[{i}] ==> ", dp[i])
                    print(f"dp[{j}] + cuboids[{i}][2] ==> ", cuboids[i][2] + dp[j])
                    dp[i] = max(dp[i], dp[j] + cuboids[i][2])

        return max(dp)