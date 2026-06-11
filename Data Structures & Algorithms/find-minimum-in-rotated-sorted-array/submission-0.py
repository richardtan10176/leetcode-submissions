class Solution:
    def findMin(self, nums: List[int]) -> int:
        p1, p2 = 0, len(nums) - 1
        mid = 0
        res = float('inf')
        while p1 <= p2:
            mid = (p1 + p2) // 2
            print(mid)
            if nums[p2] > nums[mid]:
                p2 = mid - 1
            else:
                p1 = mid + 1
            res = min(res, nums[mid])
        return res