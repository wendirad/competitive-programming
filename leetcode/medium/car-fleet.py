class Solution:
    def calc(self, target, pos, speed):
        return (target - pos) / speed

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        d = dict(zip(position, speed))

        position.sort(reverse=True)

        current = None
        ans = 0
        print(position)
        for p in position:
            val = self.calc(target, p, d[p])
            if current is None:
                ans = 1
                current = val
            elif val > current:
                ans += 1
                current = val

        return ans
