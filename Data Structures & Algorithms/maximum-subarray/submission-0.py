class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        curr = nums[0]

        for i in range(1,len(nums)):
            curr = max(nums[i], nums[i] + curr)
            ans = max(curr, ans)

        return ans