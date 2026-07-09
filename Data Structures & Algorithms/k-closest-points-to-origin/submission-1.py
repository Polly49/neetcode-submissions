class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import math
        a=[]
        ans=[]
        for n in points:
            b=math.sqrt(n[0]**2+n[1]**2)
            a.append((b,n))
        heapq.heapify(a)
        for i in range(k):
            ans.append(heapq.heappop(a)[1])
        return ans
