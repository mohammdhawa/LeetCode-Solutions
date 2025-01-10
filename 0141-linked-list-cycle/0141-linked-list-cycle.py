# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        node = head
        ht = set()
        while node:
            if node in ht:
                return True
            ht.add(node)
            node = node.next
        return False
        