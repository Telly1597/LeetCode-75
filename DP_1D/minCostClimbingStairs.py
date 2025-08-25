from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        step_1, step_2 = 0, 0
        for i in range(2, len(cost) + 1):
            step_1, step_2 = step_2, min(step_2 + cost[i - 1], step_1 + cost[i - 2])
        return step_2