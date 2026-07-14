class TimeMap:

    def __init__(self):
        self.store={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key]=[]
        self.store[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        i=0
        if key not in self.store:
            return ""
        j=len(self.store[key])-1
        a=self.store[key]
        while i<=j:
            mid=(i+j)//2
            if a[mid][1]==timestamp:
                return a[mid][0]
            elif a[mid][1]>timestamp:
                j=mid-1
            else:
                i=mid+1
        if j==-1:
            return ""
        return a[j][0]
