# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return False

        # # Approach 1: Using recursive approach
        # def check_symmetry(left, right):
        #     print(f"\n\nleft is {left} and \nright is {right}")
        #     if not left and not right:
        #         return True
        #     if not left or not right:
        #         return False
        #     if not left.val == right.val:
        #         return False
        #     return check_symmetry(left.left, right.right) and check_symmetry(left.right, right.left)
        # return check_symmetry(root.left, root.right)

        # Approach 2: using iterative approach
        from collections import deque
        queue = deque([(root.left, root.right)])
        while queue:
            left, right = queue.popleft()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))
        return True
            