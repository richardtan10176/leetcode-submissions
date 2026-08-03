class Solution:
    def climbStairs(self, n: int) -> int:
        x, y = 1, 1
        for _ in range(n - 1):
            x, y = y, y + x
        return y
