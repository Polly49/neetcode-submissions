class Solution:
    def findMin(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        while i<j:
            mid=(i+j)//2
            if nums[mid]>nums[-1]:
                i=mid+1
            elif nums[mid]<nums[-1]:
                j=mid
        
        return nums[j]
            