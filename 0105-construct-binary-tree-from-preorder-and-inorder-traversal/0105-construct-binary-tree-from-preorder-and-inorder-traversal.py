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


        # # Approach 1: Brute force
        # root_val = preorder[0]
        # root = TreeNode(val = root_val)

        # root_inorder_index = inorder.index(root_val)

        # # partition sub trees
        # left_inorder_subtree = inorder[:root_inorder_index]
        # right_inorder_subtree = inorder[root_inorder_index+1:]

        # left_preorder_subtree = preorder[1:1+len(left_inorder_subtree)]
        # right_preorder_subtree = preorder[1+len(left_inorder_subtree):]

        # root.left = self.buildTree(left_preorder_subtree, left_inorder_subtree)
        # root.right = self.buildTree(right_preorder_subtree, right_inorder_subtree)

        # return root

        # Approach 2: Optimal
        val_map = {val: idx for idx, val in enumerate(inorder)}

        def _build_tree(preorder_start, preorder_end, inorder_start, inorder_end):
            nonlocal preorder, inorder, val_map
            if preorder_start > preorder_end or inorder_start > inorder_end:
                return None
            
            root_val = preorder[preorder_start]
            root = TreeNode(val = root_val)

            # partition sub trees
            root_inorder_index = val_map.get(root_val)
            left_subtree_size = root_inorder_index - inorder_start

            preorder_left, preorder_right = (preorder_start + 1, preorder_start + left_subtree_size), (preorder_start + left_subtree_size + 1, preorder_end) # left and right
            inorder_left, inorder_right = (inorder_start, root_inorder_index - 1), (root_inorder_index + 1, inorder_end) # left and right

            # preorder_start, preorder_end, inorder_start, inorder_end
            root.left = _build_tree(*preorder_left, *inorder_left)
            root.right = _build_tree(*preorder_right, *inorder_right)
            return root
        
        return _build_tree(0, len(preorder) - 1, 0, len(inorder) - 1)