class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = [ord(i) - ord('0') for i in num1]
        n2 = [ord(i) - ord('0') for i in num2]


        nu1 = 0
        for i in range(len(n1)):
            nu1 = nu1 * 10 + n1[i]

        nu2 = 0
        for i in range(len(n2)):
            nu2 = nu2 * 10 + n2[i]
        
        return str(nu1 * nu2)