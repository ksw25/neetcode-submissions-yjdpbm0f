from collections import defaultdict, OrderedDict
import bisect
class TimeMap:

    def __init__(self):
        self.store = defaultdict(OrderedDict)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key][timestamp]= value
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store: 
            return ""

        if timestamp in self.store[key]:
            return self.store[key][timestamp]

        temp = list(self.store[key].keys())

        foundStamp = bisect.bisect_left(temp, timestamp)

        if foundStamp==0 and temp[0]>timestamp:
            return ""


        return self.store[key][temp[foundStamp-1]]

