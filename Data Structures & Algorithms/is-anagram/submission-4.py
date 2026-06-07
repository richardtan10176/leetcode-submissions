from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s1, s2 = defaultdict(int), defaultdict(int) 
        for i, num in enumerate(s):
            s1[s[i]] += 1
            s2[t[i]] += 1

        return s1 == s2