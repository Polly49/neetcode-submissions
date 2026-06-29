class TimeMap:

    def __init__(self):
        self.a={}
        self.left=float('inf')
        self.right=float('-inf')
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.a:
            self.a[key].append([timestamp,value])
        else:
            self.a[key]=[]
            self.a[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        ans=""
        if key in self.a:
            i=0
            j=len(self.a[key])-1
            while(i<=j):
                mid=(i+j)//2
                if self.a[key][mid][0]<=timestamp:
                    ans=self.a[key][mid][1]
                    i=mid+1
                elif self.a[key][mid][0]>timestamp:
                    j=mid-1
        return ans





        
