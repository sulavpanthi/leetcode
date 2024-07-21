# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if not root:
            return 
        if not p and not q:
            return

        # using recursive approach
        def traversal(node, p, q):
            if not node:
                return None
            if node == p or node == q:
                return node
            left = traversal(node.left, p, q)
            right = traversal(node.right, p, q)
            if left and right:
                return node
            return left if left else right
        
        return traversal(root, p, q)