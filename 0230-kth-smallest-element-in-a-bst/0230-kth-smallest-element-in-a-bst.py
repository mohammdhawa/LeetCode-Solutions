# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root, k: int) -> int:
        def inorder(root):
            if not root:
                return

            yield from inorder(root.left)
            yield root.val
            yield from inorder(root.right)

        gen = inorder(root)
        for _ in range(k):
            result = next(gen)
        return result
        