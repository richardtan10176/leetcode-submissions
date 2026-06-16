# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next == None:
            return head
        l,m,r = None, head, head.next
        while r:
            m.next = l
            l = m
            m = r
            r = r.next
        m.next = l
        return m
            
