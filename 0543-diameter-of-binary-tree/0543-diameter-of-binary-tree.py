# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(node):
            if not node: return 0, 0
            l_height, l_diameter = height(node.left)
            r_height, r_diameter = height(node.right)
            node_height = max(l_height, r_height) + 1
            node_diameter = l_height + r_height
            max_diameter = max(l_diameter, r_diameter, node_diameter)
            return node_height, max_diameter
        height, diameter = height(root)
        return diameter
        