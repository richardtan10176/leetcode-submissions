class Solution:
    def minWindow(self, s: str, t: str) -> str:
        p1, p2 = 0, 0
        tgt = defaultdict(int)
        win = defaultdict(int)
        res = ""
        formed = 0 #number of unique characters
        for c in t:
            tgt[c] += 1
        while p2 < len(s):
            if s[p2] in tgt:
                win[s[p2]] += 1
                if win[s[p2]] == tgt[s[p2]]:
                    formed += 1
            if formed == len(tgt):
                while formed == len(tgt):
                    if s[p1] in tgt:
                        win[s[p1]] -= 1
                        if win[s[p1]] < tgt[s[p1]]:
                            formed -= 1
                    if p2+1 - p1 < len(res) or len(res) == 0:
                        res = s[p1:p2+1]
                    p1 += 1
                    

                    
                    
            p2 += 1
        return res
