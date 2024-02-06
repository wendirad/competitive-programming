class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = ""
        for i in s.upper():
            if i.isalnum():
                n += i

        l = len(n)
        for i in range(l // 2):
            if n[i] != n[l - i - 1]:
                return False

        return True
