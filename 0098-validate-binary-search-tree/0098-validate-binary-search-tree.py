# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _inorder(self, root, mylist):
        if not root:
            return
        self._inorder(root.left, mylist)
        mylist.append(root.val)
        self._inorder(root.right, mylist)

    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        mylist = []
        self._inorder(root, mylist)
        return mylist == sorted(set(mylist))
        
        