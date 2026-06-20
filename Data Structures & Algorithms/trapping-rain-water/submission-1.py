class Solution:
    def trap(self, height: List[int]) -> int:
        left=[height[0]]*len(height)
        right=[height[-1]]*len(height)
        sum=0
        for i in range(1,len(height)):
            if(height[i]>left[i-1]):
                left[i]=height[i]
            else:
                left[i]=left[i-1]
        for j in range(len(height)-2,-1,-1):
            if(height[j]>right[j+1]):
                right[j]=height[j]
            else:
                right[j]=right[j+1]
        for i in range(0,len(height)):
            sum+=min(right[i],left[i])-height[i]
        return sum


                