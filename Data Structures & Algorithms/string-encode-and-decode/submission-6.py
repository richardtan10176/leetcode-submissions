class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}#"
            res += s
        print(res)
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = s.index('#', i)
            length = int(s[i:j])
            res.append(s[j+1:j + length+1])
            i = j + length + 1

        return res
