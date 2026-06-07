class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1, p2 = 0, 0
        res = 0
        st = set()
        while p2 < len(s):
            while s[p2] in st:
                st.remove(s[p1])
                p1 += 1
            st.add(s[p2])
            res = max(res, p2 - p1 + 1)
            p2 += 1
        return res
