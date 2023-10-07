from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash = defaultdict(int)

        for i in s:
            hash[i] += 1
        
        for i in t:
            hash[i] -= 1
        
        for i in hash.values():
            if i != 0:
                return False
        
        return True