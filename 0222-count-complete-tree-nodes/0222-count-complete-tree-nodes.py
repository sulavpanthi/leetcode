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
        
        # # Approach 1: Brute force
        # result = 0
        # queue = deque([root])
        # while queue:
        #     node = queue.popleft()
        #     result += 1
        #     if node.left:
        #         queue.append(node.left)
        #     if node.right:
        #         queue.append(node.right)
        # return result

        # Approach 2: Optimal
        def left_height(node):
            height = 0
            while node:
                node = node.left
                height += 1
            return height

        def right_height(node):
            height = 0
            while node:
                node = node.right
                height += 1
            return height

        left_height = left_height(root)
        right_height = right_height(root)
        if left_height == right_height:
            return (1<<left_height) - 1 # 2^left_height-1
        return 1+self.countNodes(root.left)+self.countNodes(root.right)

        