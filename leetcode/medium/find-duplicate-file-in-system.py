from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        data = defaultdict(list)

        for path in paths:
            path, *files = path.split()

            for file in files:
                n, cont = file.split(".txt(")
                cont = cont[:-1]
                data[cont].append(path + '/' + n + '.txt')
        
        return [val for val in data.values() if len(val) > 1]

