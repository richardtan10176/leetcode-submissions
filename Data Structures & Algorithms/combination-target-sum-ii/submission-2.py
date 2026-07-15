class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, ss, total):
            if total == target:
                res.append(ss.copy())
                return
            if total > target or i >= len(candidates):
                return
            ss.append(candidates[i])
            dfs(i + 1, ss, total + candidates[i])
            ss.pop()
            
            nextIdx = i + 1
            while nextIdx < len(candidates) and candidates[i] == candidates[nextIdx]:
                nextIdx += 1
            dfs(nextIdx, ss, total)

        dfs(0,[],0)
        return res
            
            