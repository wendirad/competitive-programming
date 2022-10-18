from collections import defaultdict

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nxG = defaultdict(lambda : -1)
        stk = []
        for i in nums2:
            if not stk:
                stk.append(i)
            else:
                while len(stk) != 0 and i > stk[-1]:
                    top = stk.pop()
                    nxG[top] = i
                stk.append(i)
        
        return list(map(lambda x: nxG[x], nums1))