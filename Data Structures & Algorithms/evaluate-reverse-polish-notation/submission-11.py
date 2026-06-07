class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b),
        }
        stk = []
        for c in tokens:
            if c in ops:
                n1, n2 = stk.pop(), stk.pop()
                stk.append(ops[c](n2, n1))
            else:
                stk.append(int(c))
        return stk[0]