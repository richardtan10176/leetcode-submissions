class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0

        for i in range(n):
            p1, p2 = i, i
            while 0 <= p1 < n and 0 <= p2 < n and s[p1] == s[p2]:
                res += 1
                p1 -= 1
                p2 += 1
            
            p1, p2 = i, i + 1
            while 0 <= p1 < n and 0 <= p2 < n and s[p1] == s[p2]:
                res += 1
                p1 -= 1
                p2 += 1
        return res
        
