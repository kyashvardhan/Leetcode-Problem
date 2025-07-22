# Problem Statement:
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
#
# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]
#
# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Solves the Add Two Numbers problem.
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Adds two numbers represented by linked lists.

        This solution iterates through both linked lists simultaneously, simulating
        grade-school addition. We maintain a `carry` value that gets propagated
        to the next digit's calculation.

        A dummy head node is used to simplify the process of building the result
        linked list. This avoids special handling for the first node.

        The loop continues as long as there are digits in either list or there is a
        remaining carry.

        Args:
            l1: The head of the first linked list.
            l2: The head of the second linked list.

        Returns:
            The head of the resulting linked list representing the sum.
        """
        # A dummy head helps simplify the code, especially for the first node.
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        # Loop until we have processed all digits from both lists and the carry.
        while l1 is not None or l2 is not None or carry != 0:
            # Get the values of the current nodes. If a list is shorter,
            # its value is considered 0.
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0

            # Calculate the sum of the digits and the carry from the previous step.
            total_sum = val1 + val2 + carry

            # The new digit is the sum modulo 10.
            # The new carry is the integer division of the sum by 10.
            carry = total_sum // 10
            new_digit = total_sum % 10

            # Create a new node with the calculated digit and append it to the result list.
            current.next = ListNode(new_digit)
            current = current.next

            # Move to the next nodes in the input lists, if they exist.
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        # The result list starts from the node after the dummy head.
        return dummy_head.next

# Complexity Analysis:
#
# Time Complexity: O(max(m, n))
# The algorithm iterates through the linked lists once. The number of iterations
# is determined by the length of the longer list (m or n).
#
# Space Complexity: O(max(m, n))
# The length of the new linked list is at most max(m, n) + 1 (to accommodate a
# final carry). Therefore, the space required is proportional to the length of
# the longer input list.
