class Solution:
    def search(self, nums: List[int], target: int) -> int:
        p1, p2 = 0, len(nums) - 1
        while p1 < p2:
            mid = (p1 + p2) // 2
            if nums[mid] > nums[p2]:
                p1 = mid + 1
            else:
                p2 = mid
        pivot = p2
        if target <= nums[-1] and target >= nums[pivot] :
            p1, p2 = pivot, len(nums) - 1
        else:
            p1, p2 = 0, pivot - 1
        print(p1, p2)
        while p1 <= p2:
            mid = (p1 + p2) // 2
            if target < nums[mid]:
                p2 = mid - 1
            elif target > nums[mid]:
                p1 = mid + 1
            else:
                return mid
        return -1
        
            