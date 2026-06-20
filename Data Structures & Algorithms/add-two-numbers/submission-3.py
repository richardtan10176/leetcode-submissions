# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = None
        newHead = l1
        carry = sumOfNodes = 0

        while l1 and l2:
            sumOfNodes = (l1.val + l2.val + carry) % 10 
            carry = (l1.val + l2.val) // 10
            l1.val = sumOfNodes
            
            dummy = l1
            l1 = l1.next
            l2 = l2.next

        
        if l2:
            dummy.next = l2
            while l2 and carry:
                sumOfNodes = (l2.val + carry) % 10
                carry = (l2.val + carry) // 10
                l2.val = sumOfNodes
                dummy = l2
                l2 = l2.next
        else:
            while l1 and carry:
                sumOfNodes = (l1.val + carry) % 10
                carry = (l1.val + carry) // 10
                l1.val = sumOfNodes
                dummy = l1
                l1 = l1.next

        print(carry)
        if carry:
            dummy.next = ListNode(1, None)
        return newHead
            
        


        
            

            