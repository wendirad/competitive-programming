class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = [0] * len(s)

        for i, idx in enumerate(indices):
            n[idx] = s[i]

        return "".join(n)
