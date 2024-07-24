# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        if not root.left and not root.right: return 1

        queue = deque([(root, 1)]) # (node, level)
        # result = []
        max_level_sum = root.val
        min_level = 1
        while queue:
            n = len(queue)
            level_sum = 0
            for _ in range(n):
                node, level = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append((node.left, level+1))
                if node.right:
                    queue.append((node.right, level+1))
            if level_sum > max_level_sum:
                max_level_sum = level_sum
                min_level = level
        return min_level