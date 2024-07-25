# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        ## Approach 1: Using recursion
        # if val <= root.val:
        #     if not root.left:
        #         root.left = TreeNode(val = val)
        #         return
        #     self.insertIntoBST(root.left, val)
        # else:
        #     if not root.right:
        #         root.right = TreeNode(val = val)
        #         return
        #     self.insertIntoBST(root.right, val)
        
        # return root


        # Approach 2: Using iteration
        if not root:
            return TreeNode(val = val)
        node = root
        while root:
            if val <= root.val:
                if not root.left:
                    root.left = TreeNode(val = val)
                    break
                root = root.left
            else:
                if not root.right:
                    root.right = TreeNode(val = val)
                    break
                root = root.right
        return node
        