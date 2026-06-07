class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sort_s = sorted(s)
        sort_t = sorted(t)
        sorted_s = "".join(sort_s)
        sorted_t = "".join(sort_t)
        return sorted_s == sorted_t