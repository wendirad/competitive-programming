class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        prop = {'type': 0, 'color': 1, 'name': 2}

        key = prop[ruleKey]

        c = 0
        for item in items:
            if item[key] == ruleValue:
                c += 1
        
        return c