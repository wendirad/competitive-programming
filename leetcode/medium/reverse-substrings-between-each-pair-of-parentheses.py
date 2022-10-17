class Solution:
    def reverseParentheses(self, s: str) -> str:
        rev = []
        
        for i in s:
            if i != ')':
                rev.append(i)
            else:
                temp = []
                while rev[-1] != '(':
                    temp.append(rev.pop())
                rev.pop()
                rev.extend(temp)
        
        return ''.join(rev)
                    