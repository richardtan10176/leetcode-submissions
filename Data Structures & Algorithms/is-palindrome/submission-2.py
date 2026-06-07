class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1, p2 = 0, len(s) - 1
        s = s.lower()
        print(s)
        while p1 < p2:
            if not s[p1].isalnum():
                p1 += 1
                continue
            if not s[p2].isalnum():
                p2 -= 1
                continue
            if s[p2] != s[p1]:
                return False
            p1 += 1
            p2 -= 1
        return True