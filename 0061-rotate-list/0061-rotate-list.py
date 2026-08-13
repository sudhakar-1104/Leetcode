class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Empty list or single node
        if not head or not head.next:
            return head

        # Find length and last node
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        # Rotating by length gives the same list
        k %= length

        if k == 0:
            return head

        # Make the list circular
        tail.next = head

        # Find the new tail
        # New tail is at position length - k - 1
        steps = length - k

        new_tail = head
        for _ in range(steps - 1):
            new_tail = new_tail.next

        # New head comes after new tail
        new_head = new_tail.next

        # Break the circle
        new_tail.next = None

        return new_head