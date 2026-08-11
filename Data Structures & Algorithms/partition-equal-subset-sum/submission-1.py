class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        target = 0
        for num in nums:
            target += num
        if target % 2 == 1:
            return False
        target /= 2

        def dfs(i, remainder):
            if i == n:
                return False
            if remainder - nums[i] == 0:
                return True
            if remainder - nums[i] > 0:
                if dfs(i + 1, remainder - nums[i]):
                    return True
            if dfs(i + 1, remainder):
                return True
            return False

        
        return dfs(0, target)

