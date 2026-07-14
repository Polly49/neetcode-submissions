class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right= len(nums)-1
        while(left<right):
            mid=(left+right)//2
            if nums[mid]>nums[right]:
                left=mid+1
            elif nums[mid]<nums[right]:
                right=mid
        if target >=nums[right] and target<=nums[-1]:
            i=right
            j=len(nums)-1
        else:
            i=0
            j=right-1
        while i<=j:
            mid=(i+j)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                i=mid+1
            else:
                j=mid-1
            
        return -1

