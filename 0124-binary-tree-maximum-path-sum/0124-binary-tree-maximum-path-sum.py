# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def sum_and_max_sum(node):
            if not node: return 0, float("-inf")
            if not node.left and not node.right: return node.val, node.val
            
            left_sum, left_max_sum = sum_and_max_sum(node.left)
            right_sum, right_max_sum = sum_and_max_sum(node.right)
            
            total_sum = max(left_sum, right_sum, 0) + node.val
            current_max_sum = max(0, left_sum) + max(0, right_sum) + node.val
            current_max_sum = max(left_max_sum, right_max_sum, current_max_sum)

            return total_sum, current_max_sum
        _, total_max_sum = sum_and_max_sum(root)
        return total_max_sum
