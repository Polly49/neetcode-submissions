class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack:
            if self.minstack[-1]>val:
                self.minstack.append(val)
            else:
                self.minstack.append(self.minstack[-1])
        else:
            self.minstack.append(val)
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        if self.minstack:
            self.minstack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]


    def getMin(self) -> int:
        mn=self.minstack[-1]
        return mn