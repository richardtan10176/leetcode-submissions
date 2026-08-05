class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0   
        n = len(nums)
        if n < 2:
            return nums[0]
        for i in range(1, n, 1):
            rob1, rob2 = max(rob1, rob2 + nums[i]), rob1
        rob3, rob4 = 0, 0
        for i in range(0, n - 1, 1):
            rob3, rob4 = max(rob3, rob4 + nums[i]), rob3
        
        return max(rob1, rob3)