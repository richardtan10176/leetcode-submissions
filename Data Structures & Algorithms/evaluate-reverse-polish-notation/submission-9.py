class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for i in range(0, len(tokens), 1):
            c = tokens[i]
            if c == '+':
                n1 = stk.pop()
                n2 = stk.pop()
                stk.append(n2 + n1)
            elif c == '*':
                n1 = stk.pop()
                n2 = stk.pop()
                stk.append(n2 * n1)
            elif c == '-':
                n1 = stk.pop()
                n2 = stk.pop()
                stk.append(n2 - n1)
            elif c == '/':
                n1 = stk.pop()
                n2 = stk.pop()
                stk.append(int(n2 / n1))
            else:
                stk.append(int(c))

        return stk[0]