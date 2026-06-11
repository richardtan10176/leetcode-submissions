import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        Min, Max = 1, 0
        for cnt in piles:
            if cnt < Min:
                Min = cnt
            if cnt > Max:
                Max = cnt
        res = float('inf')
        print(Min, Max)
        while Min <= Max:
            k = (Min + Max) // 2
            eatingTime = 0
            for cnt in piles:
                eatingTime += math.ceil(cnt / k)
            if eatingTime > h:
                Min = k + 1
            elif eatingTime <= h:
                Max = k - 1
                
            if eatingTime <= h:
                res = min(k, res)
            print(eatingTime, k)
        return int(res)