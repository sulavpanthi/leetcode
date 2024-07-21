# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        # # Approach 1: Using recursion
        # result = []
        # max_level = -1
        # def traversal(node, level):
        #     nonlocal result, max_level
        #     if not node:
        #         return
        #     if level > max_level:
        #         result.append(node.val)
        #         max_level += 1
        #     traversal(node.right, level+1)
        #     traversal(node.left, level+1)
        # traversal(root, 0)
        # return result


        # Approach 2: Using iteration
        from collections import deque
        queue = deque([(root, 0)])
        result = []
        max_level = -1
        while queue:
            n = len(queue)
            for _ in range(n):
                node, level = queue.popleft()
                if level > max_level:
                    result.append(node.val)
                    max_level = level
                if node.right:
                    queue.append((node.right, level + 1))
                if node.left:
                    queue.append((node.left, level + 1))
        return result