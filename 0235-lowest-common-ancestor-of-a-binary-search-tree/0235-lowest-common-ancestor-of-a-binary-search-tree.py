# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        temp = root
        
        while temp:
            if p.val < temp.val and q.val < temp.val:
                temp = temp.left
            elif p.val > temp.val and q.val > temp.val:
                temp = temp.right
            else:
                return temp
        return temp
        