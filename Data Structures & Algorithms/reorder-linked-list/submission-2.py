# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return None
        mid = head
        temp = head
        while temp and temp.next:
            mid = mid.next
            temp = temp.next.next
        stk = []
        while mid:
            stk.append(mid)
            mid = mid.next
        
        l, r = head, head.next
        while r and stk:
            newNode = stk.pop()
            print(newNode.val)
            l.next = newNode
            newNode.next = r
            l = r
            r = r.next
        if stk:
            r.next = stk.pop()
            r.next.next = None
        else:
            r.next = None


