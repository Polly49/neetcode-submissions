class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        mx=max(piles)
        i=1
        ans=0
        while(i<=mx):
            mid=(i+mx)//2
            hr=0
            for p in piles:
                hr+=math.ceil(p/mid)
            if hr<=h:
                ans=mid
                mx=mid-1
            else:
                i=mid+1

        return ans

            

