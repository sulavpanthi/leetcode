# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2: return
        if not list2: return list1
        if not list1: return list2
        p1 = list1
        p2 = list2
        dummy = temp = ListNode(-1)
        while (p1 and p2):
            if p1.val <= p2.val:
                temp.next = p1
                temp = p1
                p1 = p1.next
            elif p2.val < p1.val:
                temp.next = p2
                temp = p2
                p2 = p2.next

        if p1: temp.next = p1
        elif p2: temp.next = p2
        return dummy.next
        