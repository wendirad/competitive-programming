from queue import deque


class MyCircularDeque:
    def __init__(self, k: int):
        self.q = deque([], k)
        self.k = k
        self.added = 0

    def inc(self):
        self.added += 1
        if self.added > self.k:
            self.added -= 1
            return False
        return True

    def insertFront(self, value: int) -> bool:
        pos = self.inc()
        if pos:
            self.q.appendleft(value)
        return pos

    def insertLast(self, value: int) -> bool:
        pos = self.inc()
        if pos:
            self.q.append(value)
        return pos

    def deleteFront(self) -> bool:
        self.added -= 1
        if self.added < 0:
            self.added += 1
            return False
        self.q.popleft()
        return True

    def deleteLast(self) -> bool:
        self.added -= 1
        if self.added < 0:
            self.added += 1
            return False

        self.q.pop()
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[0]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[-1]

    def isEmpty(self) -> bool:
        return self.added == 0

    def isFull(self) -> bool:
        return self.added >= self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
