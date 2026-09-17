"""
PYTHON SOLUTION - Add Two Numbers
08/11/2026
TIME COMPLEXITY: O(max(N, M))
SPACE COMPLEXITY: O(max(N, M))
"""
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

##############
## SOLUTION ##
##############
class Solution:
    
    ##########################
    ## ADD TWO NUMBERS      ##
    ##########################
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        ####################
        ## EDGE CASE      ##
        ####################
        # Both lists are guaranteed non-empty per constraints,
        # so no special empty-list handling is needed here.
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Simulate elementary school addition, digit by digit
        # KEY INSIGHT: Since digits are stored in REVERSE order (least
        # significant digit first), we can add corresponding nodes directly
        # from left to right in the lists - no need to reverse anything!
        #
        # Walk both lists simultaneously:
        #   1. Add current digits from l1, l2, PLUS any carry from before
        #   2. The new digit is (sum % 10), the new carry is (sum // 10)
        #   3. Continue until BOTH lists are exhausted AND no carry remains
        
        # Dummy node simplifies building the result list (no special-casing the head)
        dummy = ListNode(0)
        current = dummy
        
        carry = 0
        
        # Continue as long as there's a digit left in EITHER list, OR a carry to add
        while l1 or l2 or carry:
            # Get current digit values (0 if that list has already ended)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Compute the sum for this position, including carry from before
            total = val1 + val2 + carry
            
            # Extract this digit and the new carry
            carry = total // 10
            digit = total % 10
            
            # Attach the new digit as a node in the result list
            current.next = ListNode(digit)
            current = current.next
            
            # Advance to next nodes in each list (if they exist)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        # Real result starts after the dummy node
        return dummy.next

#########
## EOF ##
#########