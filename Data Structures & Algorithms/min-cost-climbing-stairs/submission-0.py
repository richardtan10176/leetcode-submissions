class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first, second = 0, 0
        for c in reversed(cost):
            first, second = c + min(first, second), first
        return min(first, second)