# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True

        def check(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return check(node.left, low, node.val) and check(node.right, node.val, high)

        return check(root, float("-inf"), float("inf"))