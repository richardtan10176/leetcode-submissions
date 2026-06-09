class Solution:
    def search(self, nums: List[int], target: int) -> int:
        p1, p2 = 0, len(nums) - 1
        while p1 <= p2:
            mid = (p1 + p2) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                p2 = mid - 1
            else:
                p1 = mid + 1
        return -1