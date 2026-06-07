from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(int)
        for i, num in enumerate(nums):
            d[num] = i

        for i, num in enumerate(nums):
            conj = target-num
            if conj in d and d[conj] != i:
                return [i, d[conj]]
        
