class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        num=[]
        stack=[]
        fleet=0
        for i in range(0,len(position)):
            num.append([position[i],speed[i]])
        num=sorted(num,key=lambda x:x[0],reverse=True)
        for p,s in num:
            stack.append((target-p)/s)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)

        



        
