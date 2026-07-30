class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = float('-inf')

        for i in range(len(nums)):
            prod = 1
            for j in range(i, len(nums)):
                prod *= nums[j]
                ans = max(ans, prod)

        return ans