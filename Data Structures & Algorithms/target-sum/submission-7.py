class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total = sum(nums)

        dp = [[-1] * (total * 2 + 1) for _ in range(n + 1)]
        def findWays(i, curSum): # how many ways can we find target with nums[i:], curSum
            if i == n:
                return 1 if curSum == target else 0
            if dp[i][curSum + total] != -1:
                return dp[i][curSum + total]
            ways = findWays(i + 1, curSum - nums[i]) + findWays(i + 1, curSum + nums[i])
            dp[i][curSum + total] = ways
            return dp[i][curSum + total]
        findWays(0, 0)
        return dp[0][total]

