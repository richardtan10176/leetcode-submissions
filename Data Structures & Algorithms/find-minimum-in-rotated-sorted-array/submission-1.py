class Solution:
    def findMin(self, nums: List[int]) -> int:
        p1, p2 = 0, len(nums) - 1
        while p1 < p2:
            mid = (p1 + p2) // 2
            if nums[mid] > nums[p2]:
                p1 = mid + 1
            else:
                p2 = mid
        return nums[p1]