class TimeMap:

    def __init__(self):
        self.timestampMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timestampMap:
            self.timestampMap[key] = [[value, timestamp]]
        else: 
            self.timestampMap[key].append([value, timestamp])

        # {alice: [["happy", 1], ["sad", 3]]}

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestampMap:
            return ""
        res = ""
        ls = self.timestampMap[key] # [["happy", 1], ["sad", 3], ["sad", 6], ["happy", 9], ["happy", 11]] , t = 3
        if ls[-1][1] == timestamp:
            return ls[-1][0]
        l = 0
        r = len(ls) - 1
        while l <= r:
            m = (l + r) // 2
            if ls[m][1] == timestamp:
                return ls[m][0]
            if ls[m][1] <= timestamp:
                res = ls[m][0]
                l = m + 1
            elif ls[m][1] > timestamp:
                r = m - 1
        return res

        # [["key1", 10]]
