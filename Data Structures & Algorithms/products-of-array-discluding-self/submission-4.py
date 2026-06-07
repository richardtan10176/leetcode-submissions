class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftPrefix, rightPrefix = [], []
        curSum = 1
        for i, num in enumerate(nums):
            curSum *= num
            leftPrefix.append(curSum)
        curSum = 1
        for i, num in reversed(list(enumerate(nums))):
            curSum *= num
            rightPrefix.append(curSum)
        rightPrefix.reverse()

        res = []
        for i, num in enumerate(nums):
            if i == 0:
                res.append(rightPrefix[1])
            elif i == len(nums) - 1:
                res.append(leftPrefix[i-1])
            else:
                res.append(leftPrefix[i-1] * rightPrefix[i+1])
      
        return res