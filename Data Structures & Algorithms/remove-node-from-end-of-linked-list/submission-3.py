# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        l = 0
        temp = head
        while temp:
            l += 1
            temp = temp.next
        i = 0
        dummy = None
        temp = head
        while i < (l-n):
            dummy = temp
            temp = temp.next
            i += 1
        if dummy:
            dummy.next = temp.next
        else:
            head = head.next
        return head