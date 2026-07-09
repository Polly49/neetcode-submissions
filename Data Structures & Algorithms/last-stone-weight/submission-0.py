class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq=[]
        for n in stones:
            heapq.heappush(pq,-n)
        while len(pq)>1:
            a=heapq.heappop(pq)
            heapq.heapify(pq)
            b=heapq.heappop(pq)
            heapq.heapify(pq)
            heapq.heappush(pq,a-b)
        return -pq[0]
