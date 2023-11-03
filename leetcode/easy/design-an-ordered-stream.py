class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.sol = [0] * self.n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.sol[idKey-1] = value

        ans = []
        while self.ptr < self.n and self.sol[self.ptr] != 0:
            ans.append(self.sol[self.ptr])
            self.ptr += 1
        return ans
        

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)