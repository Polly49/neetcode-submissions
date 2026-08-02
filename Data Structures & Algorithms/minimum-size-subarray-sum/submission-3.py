class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, j = 0, 0
        n = len(nums)
        sm = 0
        ans = float('inf')

        while j < n:
            sm += nums[j]

            if sm < target:
                j += 1

            else:
                while sm >= target:
                    ans = min(ans, j - i + 1)
                    sm -= nums[i]
                    i += 1
                j += 1

        return 0 if ans == float('inf') else ans