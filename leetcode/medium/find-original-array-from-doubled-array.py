from collections import defaultdict


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n % 2 == 1:
            return []

        changed.sort()

        org = []

        freq = defaultdict(int)
        for i in changed:
            freq[i] += 1

        for i in changed:
            if freq[i] < 1:
                continue
            elif freq[i * 2] > 0:
                org.append(i)
                freq[i] -= 1
                freq[i * 2] -= 1
            else:
                return []

        return org
