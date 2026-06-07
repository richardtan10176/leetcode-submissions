class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dick = dict()

        for x, n in enumerate(nums):
            dick[n] = x

        for x, n in enumerate(nums):
            conj = target - n
            if conj in dick and dick[conj] != x:
                return [x, dick[conj]]
        return []
        
        