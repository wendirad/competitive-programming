# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s = ''
        current = head
        while current is not None:
            s += str(current.val)
            current = current.next
        if s and s == s[::-1]:
            return True    
        return False