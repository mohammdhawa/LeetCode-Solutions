# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _insert(self, root, val):
        if not root:
            return TreeNode(val)

        current = root
        while current:
            if val < current.val:
                if not current.left:
                    current.left = TreeNode(val)
                    break
                current = current.left
            elif val > current.val:
                if not current.right:
                    current.right = TreeNode(val)
                    break
                current = current.right
        return root

    def sortedArrayToBST(self, nums):
        root = None
        def binary_search2(arr, l, r):
            if l > r:
                return

            mid = (l + r) // 2
            if arr[mid] is not None:
                nonlocal root
                root = self._insert(root, arr[mid])
                arr[mid] = None
            binary_search2(arr, l, mid - 1)
            binary_search2(arr, mid + 1, r)
        binary_search2(nums, 0, len(nums) - 1)
        return root
        