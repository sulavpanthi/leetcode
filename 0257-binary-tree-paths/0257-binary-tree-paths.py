# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root: return []
        if not root.left and not root.right: return [str(root.val)]

        paths = []
        queue = deque([(root, str(root.val))])

        while queue:
            node, parent = queue.popleft()
            if not node.left and not node.right:
                paths.append(parent)
            if node.left:
                queue.append((node.left, f"{parent}->{node.left.val}"))
            if node.right:
                queue.append((node.right, f"{parent}->{node.right.val}"))
        
        return paths
