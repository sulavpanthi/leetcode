# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        # # Approach 1: Using dfs
        # result = []
        # def dfs(node):
        #     if not node:
        #         result.append("X")
        #         return
        #     result.append(str(node.val))
        #     dfs(node.left)
        #     dfs(node.right)
        # dfs(root)
        # return ",".join(result)

        # Approach 2: Using level order traversal
        queue = deque([root])
        result = []
        while queue:
            node = queue.popleft()
            if not node:
                result.append("X")
            else:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        return ",".join(result)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        # # Approach 1: Using dfs
        # def dfs():
        #     value = values.pop(0)
        #     if value == 'X':
        #         return None
        #     root = TreeNode(val = value)
        #     root.left = dfs()
        #     root.right = dfs()
        #     return root

        # values = data.split(",")
        # root = dfs()
        # return root

        # Approach 2: Using level order traversal
        if not data:
            return None
        values = data.split(",")
        if values[0] == 'X':
            return None
        root = TreeNode(val = int(values[0]))
        queue = deque([root])
        i = 1
        while queue:
            node = queue.popleft()
            if values[i] != 'X':
                node.left = TreeNode(val = int(values[i]))
                queue.append(node.left)
            i += 1

            if values[i] != 'X':
                node.right = TreeNode(val = int(values[i]))
                queue.append(node.right)
            i += 1
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))