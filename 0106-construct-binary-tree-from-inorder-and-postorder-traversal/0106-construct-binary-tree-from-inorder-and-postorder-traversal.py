# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        if not inorder or not postorder:
            return None

        # # Approach 1: Brute force
        # root_val = postorder[-1]
        # root = TreeNode(val = root_val)

        # inorder_root_index = inorder.index(root_val)

        # # partition the sub arrays
        # left_inorder = inorder[:inorder_root_index]
        # right_inorder = inorder[inorder_root_index + 1:]
        # left_postorder = postorder[:len(left_inorder)]
        # right_postorder = postorder[len(left_inorder):-1]

        # root.left = self.buildTree(left_inorder, left_postorder)
        # root.right = self.buildTree(right_inorder, right_postorder)

        # return root

        # Approach 2: Optimal

        val_map = {val: idx for idx, val in enumerate(inorder)}

        def _build_tree(inorder_start, inorder_end, postorder_start, postorder_end):
            nonlocal inorder, postorder, val_map
            if inorder_start > inorder_end or postorder_start > postorder_end:
                return None
            
            root_val = postorder[postorder_end]
            root = TreeNode(val = root_val)
            root_inorder_index = val_map.get(root_val)

            left_subarray_size = root_inorder_index - inorder_start

            inorder_left, inorder_right = (inorder_start, root_inorder_index - 1), (root_inorder_index + 1, inorder_end)
            postorder_left, postorder_right = (postorder_start, postorder_start + left_subarray_size - 1), (postorder_start + left_subarray_size, postorder_end - 1)

            root.left = _build_tree(*inorder_left, *postorder_left)
            root.right = _build_tree(*inorder_right, *postorder_right)

            return root

        return _build_tree(0, len(inorder) - 1, 0, len(postorder) - 1)



        