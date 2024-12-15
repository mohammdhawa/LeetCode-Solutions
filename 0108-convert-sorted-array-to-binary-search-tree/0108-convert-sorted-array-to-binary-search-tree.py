# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None

        def bs(arr, l, r):
            if l > r:
                return None

            mid = (l + r) // 2
            node = TreeNode(arr[mid])

            node.left = bs(arr, l, mid - 1)
            node.right = bs(arr, mid + 1, r)

            return node

        return bs(nums, 0, len(nums) - 1)