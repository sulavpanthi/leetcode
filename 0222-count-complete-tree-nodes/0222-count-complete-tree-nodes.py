# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        result = 0
        queue = deque([root])
        while queue:
            node = queue.popleft()
            result += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result