class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dictS = dict()
        dictT = dict()
        for x in s:
            dictS[x] = dictS.get(x, 0) + 1
        for x in t:
            dictT[x] = dictT.get(x, 0) + 1

        return dictS == dictT