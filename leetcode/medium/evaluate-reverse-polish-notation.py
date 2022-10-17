class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        vals = []
        for t in tokens:
            if t.replace('-', '').isdigit():
                vals.append(t)
            else:
                y = vals.pop()
                x = vals.pop()
                ans = int(eval(f'{x}{t}{y}'))
                vals.append(ans)

                
                
        return vals[0]