# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        r = head
        while i < n:
            r = r.next
            i += 1


        dummy = None
        temp = head
        while r:
            dummy = temp
            temp = temp.next
            r = r.next
        
        if dummy:
            dummy.next = temp.next
        else:
            head = head.next
        return head