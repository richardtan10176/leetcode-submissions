class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        p1, p2 = 0, 0
        st = set()
        res = 1
        curLen = 0
        while p2 < len(s):
            if s[p2] not in st:
                st.add(s[p2])
                curLen += 1
                p2 += 1
            else:
                while s[p2] in st:
                    st.remove(s[p1])
                    p1 += 1
                    curLen -= 1
            res = max(curLen, res)
            print(st)

        return res