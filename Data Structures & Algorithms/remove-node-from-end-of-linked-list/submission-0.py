# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left, right, temp = head, head, None
        for x in range(n):
            right = right.next
        
        while right:
            right = right.next
            temp = left
            left = left.next
        
        if temp:
            temp.next = left.next
        else:
            return head.next

        return head

        

        
        