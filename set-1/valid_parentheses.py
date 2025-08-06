# Problem Statement:
# Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.
#
# Example 1:
# Input: s = "()"
# Output: true
#
# Example 2:
# Input: s = "()[]{}"
# Output: true
#
# Example 3:
# Input: s = "(]"
# Output: false

class Solution:
    """
    Solves the Valid Parentheses problem.
    """
    def isValid(self, s: str) -> bool:
        """
        Determines if a string of parentheses is valid using a stack.

        This solution uses a stack (implemented as a list in Python) to keep
        track of open brackets. A hash map is used to store the mappings
        of closing brackets to their corresponding opening brackets.

        The logic is as follows:
        - Iterate through each character in the string.
        - If the character is a closing bracket:
          - Check if the stack is not empty.
          - Pop the top element from the stack.
          - If the popped element does not match the corresponding opening
            bracket for the current closing bracket, the string is invalid.
        - If the character is an opening bracket, push it onto the stack.

        After iterating through the entire string, if the stack is empty, it means
        all opening brackets were correctly matched and closed. If the stack is
        not empty, it means there are unclosed opening brackets.

        Args:
            s: The input string containing parentheses.

        Returns:
            True if the string is valid, False otherwise.
        """
        # A stack to keep track of opening brackets.
        stack = []
        # A map to hold the matching pairs.
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            # If the character is a closing bracket.
            if char in mapping:
                # Pop the top element from the stack if it's not empty,
                # otherwise assign a dummy value '#' to top_element.
                top_element = stack.pop() if stack else '#'

                # If the mapping for the closing bracket doesn't match the
                # element we just popped, the string is invalid.
                if mapping[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push it onto the stack.
                stack.append(char)

        # If the stack is empty, all brackets were matched correctly.
        # Otherwise, there are unmatched opening brackets.
        return not stack

# Complexity Analysis:
#
# Time Complexity: O(n)
# We iterate through the string of length `n` exactly once. Each push and pop
# operation on the stack takes O(1) time.
#
# Space Complexity: O(n)
# In the worst-case scenario, the string consists of only opening brackets
# (e.g., "((((("), and we would have to store all `n` characters in the stack.
