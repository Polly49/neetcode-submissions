class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        p=[]
        for n in stones:
            heapq.heappush(p,-n)
        while len(p)>1:
            a=heapq.heappop(p)
            b=heapq.heappop(p)
            heapq.heappush(p,a-b)
        return -p[0]