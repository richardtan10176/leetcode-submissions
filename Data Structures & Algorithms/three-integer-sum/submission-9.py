class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        if len(nums) == 3:
            if nums[0] + nums[1] + nums[2] == 0:
                return [[nums[0], nums[1], nums[2]]]
            else:
                return []
        x = 0
        while x < len(nums) - 3:
            i = x + 1
            j = len(nums) - 1
            while i < j:
                if nums[x] + nums[i] + nums[j] == 0:
                    res.append([nums[x], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while nums[i - 1] == nums[i] and i < j:
                        i += 1
                    while nums[j + 1] == nums[j] and i < j:
                        j -= 1
                elif nums[x] + nums[i] + nums[j] > 0:
                    j -= 1
                else:
                    i += 1
            x += 1
            while nums[x - 1] == nums[x] and x < len(nums) - 3:
                x += 1
        return res