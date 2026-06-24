class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Optimal
        from collections import deque
        l=r=0
        output=[]
        q=deque()
        while(r<len(nums)):
            # pop smaller value from q
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            q.append(r)
            # remove left val from window
            if l>q[0]:
                q.popleft()
            
            if r-l+1==k:
                output.append(nums[q[0]])
                l+=1
            r+=1
        return output
            
            
                

                

