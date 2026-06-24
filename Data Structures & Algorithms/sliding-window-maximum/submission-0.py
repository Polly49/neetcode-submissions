class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Brute Force
        ans=[]
        for i in range(0,len(nums)):
            a=[]
            if i+k<=len(nums):
                a=nums[i:i+k]
                ans.append(max(a))
        return ans
        