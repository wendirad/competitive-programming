class Solution:
    def isPalindrome(self, x: int) -> bool:
        # toString = str(x)

        # n = len(toString)

        # for i in range(n//2):
        #     if toString[i] != toString[-1 - i]:
        #         return False
        
        # return True


        if str(x) == str(x)[::-1]:
            return True
        return False
