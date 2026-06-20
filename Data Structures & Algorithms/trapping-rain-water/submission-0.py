class Solution:
    def trap(self, height: List[int]) -> int:
        left=[height[0]]*len(height)
        right=[height[-1]]*len(height)
        sum=0
        for i in range(1,len(height)):
            left[i]=max(left[i-1],height[i])
        for j in range(len(height)-2,-1,-1):
            right[j]=max(right[j+1],height[j])
        for i in range(0,len(height)):
            sum+=min(right[i],left[i])-height[i]
        return sum


                