class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None

        stk = []
        while second:
            stk.append(second)
            second = second.next

        l, r = head, head.next
        while stk:
            node = stk.pop()
            l.next = node
            if r:
                node.next = r
                l = r
                r = r.next
            else:
                node.next = None
                l = node