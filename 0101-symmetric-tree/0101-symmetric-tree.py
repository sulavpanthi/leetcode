# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return False

        def check_symmetry(left, right):
            print(f"\n\nleft is {left} and \nright is {right}")
            if not left and not right:
                return True
            if not left or not right:
                return False
            if not left.val == right.val:
                return False
            return check_symmetry(left.left, right.right) and check_symmetry(left.right, right.left)
        return check_symmetry(root.left, root.right)