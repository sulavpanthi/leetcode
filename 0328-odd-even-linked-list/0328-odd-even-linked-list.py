# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head

        second_head = even = head.next
        odd = head

        while even and even.next:
            # check only even because even is always behind odd
            odd.next = odd.next.next
            odd = odd.next

            even.next = even.next.next
            even = even.next

        if odd: odd.next = second_head
        else: odd = second_head
        return head