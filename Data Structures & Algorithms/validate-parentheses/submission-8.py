class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            match c:
                case '{' | '(' | '[':
                    stk.append(c)
                case '}':
                    if not stk or stk.pop() != '{':
                        return False
                case ']':
                    if not stk or stk.pop() != '[':
                        return False
                case ')':
                    if not stk or stk.pop() != '(':
                        return False


        print(stk)
        return not stk
