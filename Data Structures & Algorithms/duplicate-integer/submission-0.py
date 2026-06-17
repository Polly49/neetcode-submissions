class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        for i in range(0,len(nums)):
            seen.add(nums[i])
        if len(nums)!=len(seen):
            return True
        else:
            return False