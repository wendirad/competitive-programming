class Solution:
    def sortSentence(self, s: str) -> str:
        ordered = s.split()
        for i in s.split():
            ordered[int(i[-1]) - 1] = i[:-1]
        return " ".join(ordered)
