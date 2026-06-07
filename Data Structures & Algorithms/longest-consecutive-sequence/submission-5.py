class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = defaultdict(int)
        if not nums:
            return 0
        for num in nums:
            d[num] += 1
        res = 1
        for num in nums:
            #start of seq
            if num - 1 not in d:
                curMax = 1
                tempNum = num + 1
                while tempNum in d:
                    curMax += 1
                    tempNum += 1
                res = max(res, curMax)
        return res