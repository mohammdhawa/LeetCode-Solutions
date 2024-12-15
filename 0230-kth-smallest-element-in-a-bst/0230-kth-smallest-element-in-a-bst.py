# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root, k: int) -> int:
        def inorder(arr, root, k):
            if not root:
                return

            if len(arr) == k:
                return
            inorder(arr, root.left, k)
            arr.append(root.val)
            inorder(arr, root.right, k)

        mylist = []
        inorder(mylist, root, k)
        return mylist[k - 1]
        