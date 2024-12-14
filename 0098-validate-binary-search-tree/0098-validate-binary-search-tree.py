# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _dfs(self, root, val, child):
        if not root:
            return True
        import collections
        queue = collections.deque()
        queue.append(root)

        while queue:
            curr = queue.popleft()
            if child == 'left' and curr.val >= val:
                return False
            elif child == 'right' and curr.val <= val:
                return False
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return True

    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        l = self._dfs(root.left, root.val, 'left')
        r = self._dfs(root.right, root.val, 'right')
        if not l or not r:
            return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)
        
        