# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def findMiddle(self, head):
        if not head.next: return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def mergeList(self, head1, head2):
        if not head1 and not head2: return
        if not head1: return head2
        if not head2: return head1
        temp = dummy = ListNode(-1)
        while head1 and head2:
            if head1.val <= head2.val:
                temp.next = head1
                temp = head1
                head1 = head1.next
            else:
                temp.next = head2
                temp = head2
                head2 = head2.next
        if head1: temp.next = head1
        elif head2: temp.next = head2
        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        middle = self.findMiddle(head)
        second_head = middle.next
        middle.next = None
        left_head = self.sortList(head)
        right_head = self.sortList(second_head)
        new_head = self.mergeList(left_head, right_head)
        return new_head
