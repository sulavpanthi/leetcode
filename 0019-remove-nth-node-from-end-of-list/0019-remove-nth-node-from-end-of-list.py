# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: return head

        dummyNode = ListNode(0)
        dummyNode.next = head
        first_pointer = second_pointer = dummyNode
        for i in range(n+1):
            second_pointer = second_pointer.next
        if second_pointer is None:
            return head.next
        while second_pointer:
            first_pointer = first_pointer.next
            second_pointer = second_pointer.next
        first_pointer.next = first_pointer.next.next
        return dummyNode.next
        