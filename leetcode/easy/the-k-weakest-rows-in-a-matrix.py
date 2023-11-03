class Row:
    def __init__(self, index, soliders):
        self.index = index
        self.soliders = soliders
        self._weakness = 0
    
    def make_weak(self):
        self._weakness += 1
    
    @property
    def weakness(self):
        return self._weakness
        
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows = []
        for index, row in enumerate(mat):
            soliders = 0
            for i in row:
                if i == 1:
                    soliders += 1
                else:
                    break
            r = Row(index, soliders)
            rows.append(r)
        length = len(rows)
        
        for i in range(length-1):
            for j in range(i+1, length):
                if (
                    (rows[i].soliders < rows[j].soliders) or
                    (rows[i].soliders == rows[j].soliders and i < j)
                ):
                    rows[i].make_weak()
                elif (rows[j].soliders < rows[i].soliders):
                    rows[j].make_weak()
            
        rows.sort(key=lambda row: row.weakness, reverse=True)
        return [rows[i].index for i in range(k)]