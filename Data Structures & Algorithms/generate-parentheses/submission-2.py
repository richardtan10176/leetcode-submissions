class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(i, ss, numLeft, numRight):
            if numRight > numLeft:
                return
            if i >= n*2:
                if numRight != numLeft:
                    return
                res.append(ss)
                return
            
            ss += '('
            dfs(i + 1, ss, numLeft + 1, numRight)
            ss = ss[:-1]
            
            ss += ')'
            dfs(i + 1, ss, numLeft, numRight + 1)

        dfs(0, '', 0, 0)
        return res