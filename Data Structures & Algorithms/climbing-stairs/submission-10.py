class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        prev2=2
        prev1=1
        for _ in range(3,n+1):
            curr=prev1+prev2
            prev1=prev2
            prev2=curr
        return prev2