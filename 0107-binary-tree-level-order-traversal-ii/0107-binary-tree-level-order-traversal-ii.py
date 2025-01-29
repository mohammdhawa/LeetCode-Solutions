# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _height(self, root):
        if root is None:
            return 0
        left = self._height(root.left)
        right = self._height(root.right)
        return max(left, right) + 1

    def levelOrderBottom(self, root):
        if not root:
            return []
        from collections import deque

        result = [[] for _ in range(self._height(root))]
        queue = deque()
        queue.append((root, 0))

        while queue:
            node, level = queue.popleft()
            result[level].append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return result[::-1]