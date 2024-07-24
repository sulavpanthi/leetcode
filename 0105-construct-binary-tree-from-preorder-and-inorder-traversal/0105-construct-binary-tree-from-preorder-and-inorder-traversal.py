# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root_val = preorder[0]
        root = TreeNode(val = root_val)

        root_inorder_index = inorder.index(root_val)

        # partition sub trees
        left_inorder_subtree = inorder[:root_inorder_index]
        right_inorder_subtree = inorder[root_inorder_index+1:]

        left_preorder_subtree = preorder[1:1+len(left_inorder_subtree)]
        right_preorder_subtree = preorder[1+len(left_inorder_subtree):]

        root.left = self.buildTree(left_preorder_subtree, left_inorder_subtree)
        root.right = self.buildTree(right_preorder_subtree, right_inorder_subtree)

        return root

        