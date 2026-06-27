class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        mx=0
        for i in range(0,len(heights)):
            if stack:
                if heights[i]<stack[-1][1]:
                    while stack and heights[i]<stack[-1][1]:
                        mx=max(mx,stack[-1][1]*(i-1-stack[-1][0]+1))
                        start=stack[-1][0]
                        stack.pop()
                    stack.append([start,heights[i]])
                else:
                    stack.append([i,heights[i]])

            else:
                stack.append([i,heights[i]])
        for p,h in stack:
            mx=max(mx,(len(heights)-p)*h)
        return mx