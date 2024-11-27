# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1, root2) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False

        d1 = {}
        count = 0
        q = deque()
        q.append(root1)

        while q:
            curr = q.popleft()
            if curr.left:
                q.append(curr.left)
                d1[curr.left.val] = curr.val
                count += 1

            if curr.right:
                q.append(curr.right)
                d1[curr.right.val] = curr.val
                count += 1

        q.append(root2)

        while q:
            curr = q.popleft()
            if curr.left:
                q.append(curr.left)
                if curr.val == d1.get(curr.left.val):
                    count -= 1
                else:
                    return False

            if curr.right:
                q.append(curr.right)
                if curr.val == d1.get(curr.right.val):
                    count -= 1
                else:
                    return False

        return count == 0
        