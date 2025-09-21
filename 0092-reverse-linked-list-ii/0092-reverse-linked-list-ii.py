# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Create a dummy node to handle the case where we need to reverse from the head
        dummy = ListNode(0)
        dummy.next = head
        
        # 1. Traverse to the node before the 'left' position
        pre_left = dummy
        for _ in range(left - 1):
            pre_left = pre_left.next
            
        # 2. 'start' is the first node of the sublist to be reversed
        start = pre_left.next
        
        # 3. 'then' is the node that we will move to the front of the sublist
        then = start.next
        
        # 4. Perform the reversal
        # We perform 'right - left' reversals
        for _ in range(right - left):
            # Take 'then' and place it before 'start'
            start.next = then.next
            then.next = pre_left.next
            pre_left.next = then
            # Move 'then' to the next node to be reversed
            then = start.next
            
        return dummy.next