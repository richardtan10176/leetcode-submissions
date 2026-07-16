class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(numsRemaning, ss):
            # print(ss)
            if len(ss) >= len(nums):
                res.append(ss.copy())
                return
            for i, num in enumerate(numsRemaning):
                ss.append(num)
                temp_remaning = numsRemaning[:i] + numsRemaning[i+1:]
                dfs(temp_remaning, ss)
                ss.pop()
                
        dfs(nums.copy(), [])
        return res