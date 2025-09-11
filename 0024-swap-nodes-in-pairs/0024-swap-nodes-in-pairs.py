class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node to simplify swapping head
        dummy = ListNode(0, head)
        prev = dummy
        
        while head and head.next:
            # Identify nodes to swap
            first = head
            second = head.next
            
            # Swapping
            prev.next = second
            first.next = second.next
            second.next = first
            
            # Move pointers forward
            prev = first
            head = first.next
        
        return dummy.next
