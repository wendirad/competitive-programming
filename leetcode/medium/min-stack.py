import sys

class MinStack:

    def __init__(self):
        self.st = []
        self.MIN = []
        self.LM = sys.maxsize
        

    def push(self, val: int) -> None:
        self.st.append(val)
        self.LM = min(self.LM, val)
        self.MIN.append(self.LM)
        
    def pop(self) -> None:
        self.st.pop()
        self.MIN.pop()
        if self.MIN:
            self.LM = self.MIN[-1]
        else:
            self.LM = sys.maxsize

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.MIN[-1]

