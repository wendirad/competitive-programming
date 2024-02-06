from collections import defaultdict


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dom3 = defaultdict(int)
        dom2 = defaultdict(int)
        dom1 = defaultdict(int)
        for cpdom in cpdomains:
            cnt, dom = cpdom.split()
            domc = dom.split(".")
            cnt = int(cnt)

            if len(domc) == 3:
                x, y, z = domc
                dom3[".".join(domc)] += cnt
                dom2[y + "." + z] += cnt
                dom1[z] += cnt
            elif len(domc) == 2:
                y, z = domc
                dom2[y + "." + z] += cnt
                dom1[z] += cnt
            else:
                dom1[domc[0]]

        ans = []
        ans.extend([str(val) + " " + dom for dom, val in dom2.items()])
        ans.extend([str(val) + " " + dom for dom, val in dom3.items()])
        ans.extend([str(val) + " " + dom for dom, val in dom1.items()])

        return ans
