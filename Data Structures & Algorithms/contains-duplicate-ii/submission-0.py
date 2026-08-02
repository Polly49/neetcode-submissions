class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic={}
        for i in range(0,len(nums)):
            if nums[i] in dic: 
                if i-dic[nums[i]]<=k:
                    return True
            dic[nums[i]]=i
        return False
        