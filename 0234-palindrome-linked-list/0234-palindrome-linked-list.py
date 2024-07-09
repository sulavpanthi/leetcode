# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next: return True

        # step 1: find the middle of linked list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # step 2: reverse the second half of the linked list from the middle
        second_head = slow
        prev = None
        while second_head:
            next_node = second_head.next
            second_head.next = prev
            prev = second_head
            second_head = next_node

        # step 3: use 2 pointers to check if both are same or not
        while head and prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True