# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def iterative_inorder(self, root):
        st = [(root, False)]
        result = []

        while st:
            temp, flag = st.pop()

            if flag:
                result.append(temp.val)
            else:
                if temp.right:
                    st.append((temp.right, False))
                if temp.left:
                    st.append((temp, True))
                    st.append((temp.left, False))
                else:
                    result.append(temp.val)
        return result

    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        mylist = self.iterative_inorder(root)
        return mylist == sorted(set(mylist))
        
        