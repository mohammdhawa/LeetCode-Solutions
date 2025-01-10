# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        node = head
        ht = {}
        while node:
            if ht.get(node) is not None:
                return True
            ht[node] = 1
            node = node.next
        return False
        