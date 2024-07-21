# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        max_level = -1
        def traversal(node, level):
            nonlocal result, max_level
            if not node:
                return
            if level > max_level:
                result.append(node.val)
                max_level += 1
            traversal(node.right, level+1)
            traversal(node.left, level+1)
        traversal(root, 0)
        return result