class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Empty list or single node
        if not head or not head.next:
            return head

        # Find the middle using slow and fast pointers
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split the list
        mid = slow.next
        slow.next = None

        # Sort both halves
        left = self.sortList(head)
        right = self.sortList(mid)

        # Merge the two sorted halves
        dummy = ListNode(0)
        current = dummy

        while left and right:
            if left.val <= right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next

            current = current.next

        # Attach remaining nodes
        if left:
            current.next = left
        else:
            current.next = right

        return dummy.next