class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            if not stk or temp <= temperatures[stk[-1]]:
                stk.append(i)
            elif temp > temperatures[stk[-1]]:
                while stk and temperatures[stk[-1]] < temp:
                    n = stk.pop()
                    res[n] = i - n
                stk.append(i)
        return res