class Solution:
    def do(self,token:str,a:int,b:int) -> int:
        if token=='+':
            ans=a+b
        elif token=='-':
            ans=a-b
        elif token=='*':
            ans = a*b
        elif token == '/':
            ans=int(a/b)
        return ans
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for ch in tokens:
            if ch in "+-/*":
                a=int(stack.pop())
                b=int(stack.pop())
                ans=self.do(ch,b,a) 
                stack.append(ans)
            else:
                stack.append(ch)
        if stack:
            return int(stack[-1])
        else:
            return 0  