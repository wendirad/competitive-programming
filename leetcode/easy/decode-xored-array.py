class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        orginal = [first]
        for enc in encoded:
            orginal.append(orginal[-1] ^ enc)
        
        return orginal