class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = (r - l) * min(heights[r], heights[l])
        while l < r:
            if heights[l] > heights[r]:
                r -= 1
            elif heights[r] > heights[l]:
                l += 1
            else:
                l += 1 
                r -= 1
            res = max(res, (r - l) * min(heights[r], heights[l]))
        return res
