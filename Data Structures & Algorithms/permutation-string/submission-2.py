class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        tgt = defaultdict(int)
        win = defaultdict(int)
        for i in range(len(s1)):
            tgt[s1[i]] += 1
            win[s2[i]] += 1
        p1, p2 = 0, len(s1) - 1
        while p2 < len(s2) - 1:
            print(tgt)
            print(win)
            if win == tgt:
                return True
            else:
                win[s2[p1]] -= 1
                if win[s2[p1]] == 0:
                    win.pop(s2[p1])
                p1 += 1
                p2 += 1
                win[s2[p2]] += 1
        return win == tgt

        