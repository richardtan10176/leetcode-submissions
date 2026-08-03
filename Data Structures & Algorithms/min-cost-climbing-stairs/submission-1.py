class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first, second = 0, 0

        for cst in reversed(cost):
            second, first = cst + min(first, second), second
        return min(second, first)