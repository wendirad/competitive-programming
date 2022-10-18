afrom collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        
        l = sorted(freq.items(), key=lambda x : x[1], reverse=True)
        
        m = len(tasks)
        
        nOfMax = 1
        
        for i in range(1, len(l)):
            if freq[l[i][0]] == freq[l[0][0]]:
                nOfMax += 1
            else:
                break
        space = l[0][1] - 1
        empty = space * (n -(nOfMax - 1))
        av = m - (l[0][1] * nOfMax)
        idle = max(0, empty - av)
        return m + idle
        
        