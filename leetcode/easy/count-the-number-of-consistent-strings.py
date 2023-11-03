from collections import Counter
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        srtd = Counter(allowed)
        count = 0
        for word in words:
            for char in word:
                if not srtd[char]:
                    count += 1
                    break
            
        return len(words) - count

