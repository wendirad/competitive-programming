class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        MAX = float("-inf")

        for st in sentences:
            MAX = max(MAX, len(st.split()))

        return MAX
