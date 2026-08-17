# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         n = len(nums)
#         total = sum(nums)

#         dp = {}
#         def findWays(i, curSum): # how many ways can we find target with nums[i:], curSum
#             if i == n:
#                 return 1 if curSum == target else 0
#             if (i, curSum) in dp:
#                 return dp[(i, curSum)]
#             ways = findWays(i + 1, curSum - nums[i]) + findWays(i + 1, curSum + nums[i])
#             dp[(i, curSum)] = ways
#             return dp[(i, curSum)]
#         findWays(0, 0)
#         return dp[(0, 0)]

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n + 1)]
        total = sum(nums)
        dp[n][target] = 1

        for i in range(n - 1, -1, -1):
            for curSum in range(-total, total + 1):
                dp[i][curSum] = dp[i + 1][curSum - nums[i]] + dp[i + 1][curSum + nums[i]]
        
        return dp[0][0]