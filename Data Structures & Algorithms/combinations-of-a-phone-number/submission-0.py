class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numDict = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }
        res = []
        def dfs(i, ss):
            print(ss)
            if i >= len(digits):
                if ss:
                    res.append(ss)
                return
            for letter in numDict[int(digits[i])]:
                ss += letter
                dfs(i + 1, ss)
                ss = ss[:-1]
            
        dfs(0, "")
        print(res)
        return res