class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        p1, p2 = 0, 0
        res = 0
        maxInWindow = 0
        d = defaultdict(int)
        while p2 < len(s):
            c = s[p2]
            d[c] += 1
            if d[c] > maxInWindow:
                maxInWindow = d[c]
            if p2 - p1 + 1 - maxInWindow > k:
                while p2 - p1 + 1 - maxInWindow > k:
                    d[s[p1]] -= 1
                    
                    p1 += 1
            
            res = max(res, p2 - p1 + 1)
            p2 += 1
        return res
            


                
                
            
            