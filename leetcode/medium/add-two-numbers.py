# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = None
        x, y = 0, 0
        mul = 1
        while l1 or l2:
            x += l1.val * mul if l1 else 0
            y += l2.val * mul if l2 else 0
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            mul *= 10

        result = x + y
        tail = None
        first = True
        while first or result:
            if first:
                first = False
            last = result % 10
            result //= 10

            if head is None:
                head = ListNode(last)
            else:
                if tail is None:
                    tail = ListNode(last)
                    head.next = tail
                else:
                    tail.next = ListNode(last)
                    tail = tail.next
        return head
