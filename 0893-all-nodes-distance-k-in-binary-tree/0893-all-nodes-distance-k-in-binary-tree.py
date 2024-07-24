# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:

    def traversal(self, node, height):
        """
        function to traverse upto specified height from current node
        and append to result if distance is covered
        """
        if height == 0:
            self.result.append(node.val)
            return
        queue = deque([(node, height)])
        while queue:
            n = len(queue)
            for _ in range(n):
                node, height = queue.popleft()
                if height == 0:
                    self.result.append(node.val)
                if node.left and height > 0:
                    queue.append((node.left, height - 1))
                if node.right and height > 0:
                    queue.append((node.right, height - 1))
        

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.result = []
        
        def traverse(node):
            nonlocal target, k
            if node.val == target.val:
                self.traversal(node, k)
                # return distance for backtracking for parent node
                return (k - 1) if k > 0 else None
            else:
                if node.left:
                    # find distance for backtracking
                    distance = traverse(node.left)
                    if distance is not None:
                        if distance == 0:
                            self.result.append(node.val)
                        elif distance > 0 and node.right:
                            self.traversal(node.right, distance - 1)
                        # return remaining distance for backtracking
                        return distance - 1 if distance > 0 else None

                if node.right:
                    # find distance for backtracking
                    distance = traverse(node.right)
                    if distance is not None:
                        if distance == 0:
                            self.result.append(node.val)
                        elif distance > 0 and node.left:
                            self.traversal(node.left, distance - 1)
                        # return remaining distance for backtracking
                        return distance - 1 if distance > 0 else None

        traverse(root)
        return self.result
        
            
