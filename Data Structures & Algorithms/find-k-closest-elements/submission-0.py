class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        import heapq
        heap=[]
        for n in arr:
            heap.append((abs(n-x),n))
        heapq.heapify(heap)
        ans=[]
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        return sorted(ans)
