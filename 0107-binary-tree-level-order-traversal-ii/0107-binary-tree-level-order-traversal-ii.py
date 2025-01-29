# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return []
        from collections import deque

        result = []
        queue = deque()
        queue.append((root, 0))

        while queue:
            node, level = queue.popleft()
            if level == len(result):
                result.append([])
            result[level].append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return result[::-1]