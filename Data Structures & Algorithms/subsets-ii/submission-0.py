class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(i, ss):
            if i >= len(nums):
                res.append(ss.copy())
                return
            
            ss.append(nums[i])
            dfs(i + 1, ss)
            ss.pop()

            next_idx = i + 1
            while next_idx < len(nums) and nums[next_idx] == nums[i]:
                next_idx += 1
            dfs(next_idx, ss)
        dfs(0, [])
        return res


            
        
        