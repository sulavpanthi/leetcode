# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sum = 0
        result = new_head = None
        while (head):
            sum += head.val
            if head.val == 0 and sum != 0:
                new_node = ListNode(sum)
                sum = 0
                if new_head is None:
                    result = new_head = new_node
                else:
                    new_head.next = new_node
                    new_head = new_node
            head = head.next
        return result