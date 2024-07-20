# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict
class Solution:

    def merge_dict(self, d_dict, temp):
        for key in temp.keys():
            d_dict[key].extend(sorted(temp[key]))
        return d_dict

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        result = []
        queue = [(root, 0)]
        y, y_min, y_max = 0, 0, 0
        d_dict = defaultdict(list)

        # using level order traversal and keeping that level's values in temp
        # after completing each level, merge temp's sorted values to d_dict
        while len(queue) > 0:
            n = len(queue)
            temp = defaultdict(list)
            for i in range(n):
                node, y = queue.pop(0)
                temp[y].append(node.val)
                if node.left:
                    queue.append((node.left, y-1))
                    y_min = min(y_min, y-1)
                if node.right:
                    queue.append((node.right, y+1))
                    y_max = max(y_max, y+1)
            d_dict = self.merge_dict(d_dict, temp)

        # converting dict to list at last
        for i in range(y_min, y_max+1):
            result.append(d_dict[i])
        return result

        while len(queue) > 0:
            n = len(queue)
            temp = defaultdict(list)
            for each in range(n):
                node = queue.pop(0)
                def traversal(node, y):
                    nonlocal y_min, y_max
                    d_dict[y].append(node.val)
                    if node.left:
                        y_min = min(y_min, y-1)
                        traversal(node.left, y-1)
                    if node.right:
                        y_max = max(y_max, y+1)
                        traversal(node.right, y+1)
                traversal(node, 0)
            level += 1
        for key in range(y_min, y_max+1):
            result.append(sorted(d_dict[key]))
        return result
