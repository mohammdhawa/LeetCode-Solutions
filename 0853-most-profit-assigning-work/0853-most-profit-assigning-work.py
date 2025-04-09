class Solution:
    def maxProfitAssignment(self, difficulty: list[int], profit: list[int], worker: list[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        
        max_profit = 0
        total_max_profit = 0
        i = 0
        
        for w in worker:
            while i < len(jobs) and jobs[i][0] <= w:
                max_profit = max(max_profit, jobs[i][1])
                i += 1
            total_max_profit += max_profit
        return total_max_profit