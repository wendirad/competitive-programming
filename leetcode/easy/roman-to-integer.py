class Solution:
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    def substract(self, a, b):
        pass
    
    def romanToInt(self, s: str) -> int:
        length = len(s)
        if length < 2:
            return self.romans[s]
        result = 0
        i = 0
        while i < length:
            current = s[i]
            next_ = s[i+1] if i < (length - 1) else None
            if (
                (next_ is not None) and
                (
                    (s[i] == 'I' and s[i+1] in 'VX') or 
                    (s[i] == 'X' and s[i+1] in 'LC') or 
                    (s[i] == 'C' and s[i+1] in 'DM')
                )
            ):
                result += (self.romans[s[i+1]] - self.romans[s[i]])
                i += 2
            else:
                result += self.romans[s[i]]
                i += 1
        
        return result
                
                