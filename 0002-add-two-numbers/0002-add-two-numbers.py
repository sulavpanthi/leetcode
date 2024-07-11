# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1: return l2
        if not l2: return l1
        p1, p2 = l1, l2
        temp = dummy = ListNode(-1)
        carry = 0
        while p1 and p2:
            result = p1.val + p2.val + carry
            if result < 10:
                carry = 0
            else:
                carry = 1
                result -= 10
            dummy.next = ListNode(result)
            dummy = dummy.next
            p1 = p1.next
            p2 = p2.next
        remaining = p1 or p2
        while remaining:
            result = remaining.val
            if carry > 0:
                result += carry
            if result < 10:
                carry = 0
            else:
                result -= 10
                carry = 1
            dummy.next = ListNode(result)
            dummy = dummy.next
            remaining = remaining.next
        if carry > 0:
            dummy.next = ListNode(carry)
        return temp.next
        