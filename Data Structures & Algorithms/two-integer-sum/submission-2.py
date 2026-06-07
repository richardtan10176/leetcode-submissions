from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(int)
        for i, num in enumerate(nums):
            comp = target - num
            if comp in d:
                return [d[comp], i]
            d[num] = i
        
