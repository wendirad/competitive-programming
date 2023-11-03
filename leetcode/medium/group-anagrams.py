from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for st in strs:
            d[''.join(sorted(st))].append(st)
        
        return d.values()
