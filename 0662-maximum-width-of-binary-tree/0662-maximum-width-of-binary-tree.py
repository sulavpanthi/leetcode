# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return

        level = 0
        max_width = 0
        queue = deque([(root, 0)]) # (node, index)
        while queue:
            n = len(queue)
            first_node, first_index = queue[0]
            for _ in range(n):
                node, _index = queue.popleft()
                if node.left:
                    queue.append((node.left, 2*_index+1))
                if node.right:
                    queue.append((node.right, 2*_index+2))
            last_index = _index
            width = last_index - first_index + 1
            max_width = max(max_width, width)
        return max_width
