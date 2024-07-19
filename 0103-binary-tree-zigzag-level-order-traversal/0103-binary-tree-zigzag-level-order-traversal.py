# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return 
        left_to_right = True
        res= []
        queue = [root]
        while len(queue) > 0:
            n = len(queue)
            temp = []
            for _ in range(n):
                node = queue.pop(0)
                if left_to_right:
                    temp.append(node.val)
                else:
                    temp.insert(0, node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(temp)
            left_to_right = not left_to_right
        return res
