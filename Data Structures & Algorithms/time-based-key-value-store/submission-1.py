class TimeMap:
    
    
    def __init__(self):  
        self.KV = defaultdict(tuple)
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.KV:
            self.KV[key][0].append(value)
            self.KV[key][1].append(timestamp)
        else:
            self.KV[key] = ([value], [timestamp])
            
    def get(self, key: str, timestamp: int) -> str:
        if key in self.KV:
            l = self.KV[key][1]
            print(l)
            if timestamp < l[0]:
                return ""
            p1, p2 = 0, len(l) - 1
            mid = 0
            while p1 <= p2:
                mid = (p1 + p2) // 2
                print(mid)
                if l[mid] == timestamp:
                    return self.KV[key][0][mid]
                elif l[mid] > timestamp:
                    p2 = mid - 1
                else:
                    p1 = mid + 1
            print(self.KV[key][0])
            return self.KV[key][0][p2]
            
        return ""