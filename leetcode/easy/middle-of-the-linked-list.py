# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals = []
        length = 0
        while head:
            vals.append(head)
            head = head.next
            length += 1
        middle = length // 2
        return vals[middle]
