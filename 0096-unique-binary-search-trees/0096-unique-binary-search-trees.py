class Solution:
    def numTrees(self, n: int) -> int:
        
        def factorial(x, memo={}):
            if x in memo:
                return memo[x]

            if x == 1:
                return 1
            
            memo[x] = factorial(x - 1, memo) * x
            return memo[x]

        
        memo = {}
        return int(1 / (n + 1) * (factorial(2 * n, memo) / (factorial(n, memo) * factorial(n, memo))))
