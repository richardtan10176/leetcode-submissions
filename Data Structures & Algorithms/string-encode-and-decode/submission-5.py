class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += s
            res += '♀'
        print(res)
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        curs = ""
        for c in s:
            if c == '♀':
                res.append(curs)
                curs = ""
            else:
                curs += c
        return res