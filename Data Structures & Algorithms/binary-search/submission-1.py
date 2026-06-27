class Solution:
    def search(self, nums: List[int], target: int) -> int:
        loc=-1
        start=0
        end=len(nums)-1
        while(start<=end):
            mid=start+end
            if nums[mid]==target:
                loc=mid
                return loc
            elif nums[mid]<target:
                start=mid+1
            else:
                end=mid-1
        return loc