from functools import cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        @cache
        def findWays(i, curSum): # how many ways can we find target with nums[i:], curSum
            if i == n:
                return 1 if curSum == target else 0
            
            return findWays(i + 1, curSum - nums[i]) + findWays(i + 1, curSum + nums[i])
        return findWays(0, 0)
