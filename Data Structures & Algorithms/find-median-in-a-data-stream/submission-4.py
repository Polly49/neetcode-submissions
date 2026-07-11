class MedianFinder:

    def __init__(self):
        self.smallheap=[]
        self.largeheap=[]
    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallheap,-num)
        if self.largeheap and -self.smallheap[0] > self.largeheap[0]:
            val = -heapq.heappop(self.smallheap)
            heapq.heappush(self.largeheap, val)
        if len(self.smallheap)>len(self.largeheap)+1:
            a=heapq.heappop(self.smallheap)
            heapq.heappush(self.largeheap,-a)
        elif len(self.largeheap)>len(self.smallheap)+1:
            a=heapq.heappop(self.largeheap)
            heapq.heappush(self.smallheap,-a)
        return
    def findMedian(self) -> float:
        if len(self.smallheap)==len(self.largeheap):
            return (-self.smallheap[0]+self.largeheap[0])/2.0
        elif len(self.smallheap)==len(self.largeheap)+1:
            return -self.smallheap[0]
        elif len(self.smallheap)==len(self.largeheap)-1:
            return self.largeheap[0]
            

        
        