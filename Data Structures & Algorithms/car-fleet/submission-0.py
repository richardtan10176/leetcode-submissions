class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        lst = []
        for x in range(len(position)):
            lst.append((position[x], speed[x]))

        lst.sort()
        fleetTime = -1
        res = 0
        while lst:
            car = lst.pop()
            curTime = (target - car[0]) / car[1]
            if curTime > fleetTime:
                fleetTime = curTime
                res += 1
            

        return res
