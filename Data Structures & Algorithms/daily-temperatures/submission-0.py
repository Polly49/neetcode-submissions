class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0]*len(temperatures)
        stack=[]
        for j in range(0,len(temperatures)):
            if stack:
                while stack and temperatures[stack[-1]]<temperatures[j]:
                    ans[stack[-1]]=j-stack[-1]
                    stack.pop()
                stack.append(j)
            else:
                stack.append(j)
        return ans