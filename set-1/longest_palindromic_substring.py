# Problem Statement:
# Given a string `s`, return the longest palindromic substring in `s`.
#
# A string is a palindrome if it reads the same backward as forward.
#
# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
#
# Example 2:
# Input: s = "cbbd"
# Output: "bb"

class Solution:
    """
    Solves the Longest Palindromic Substring problem.
    """
    def longestPalindrome(self, s: str) -> str:
        """
        Finds the longest palindromic substring in a given string.

        This solution uses the "Expand From Center" approach. The main idea is
        that every palindrome has a center. This center can be a single character
        (for odd-length palindromes like "racecar") or a pair of characters
        (for even-length palindromes like "aabbaa").

        We iterate through each character of the string and treat it as a potential
        center for a palindrome. For each character, we check for two cases:
        1. The palindrome is odd-length (centered at the character itself).
        2. The palindrome is even-length (centered between the character and the next one).

        We expand outwards from the center as long as the characters on both sides
        match. We keep track of the start and end indices of the longest
        palindrome found so far.

        Args:
            s: The input string.

        Returns:
            The longest palindromic substring.
        """
        if not s or len(s) < 1:
            return ""

        start = 0
        end = 0

        for i in range(len(s)):
            # Case 1: Odd-length palindrome (center is s[i])
            len1 = self._expand_from_center(s, i, i)
            # Case 2: Even-length palindrome (center is between s[i] and s[i+1])
            len2 = self._expand_from_center(s, i, i + 1)
            
            # Find the maximum length from the two cases
            current_max_len = max(len1, len2)

            # If we found a new longest palindrome, update the start and end indices
            if current_max_len > (end - start):
                # Calculate new start and end based on the center and length
                start = i - (current_max_len - 1) // 2
                end = i + current_max_len // 2
        
        # Return the longest palindromic substring using the final indices
        return s[start : end + 1]

    def _expand_from_center(self, s: str, left: int, right: int) -> int:
        """
        Helper function to expand from a center and find the length of the palindrome.
        
        Args:
            s: The input string.
            left: The left pointer of the center.
            right: The right pointer of the center.

        Returns:
            The length of the palindrome found.
        """
        # Expand as long as pointers are in bounds and characters match
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        # The length of the palindrome is right - left - 1
        return right - left - 1

# Complexity Analysis:
#
# Time Complexity: O(n^2)
# We iterate through the string of length n. For each character, we might expand
# outwards up to n/2 times in both directions. This gives a quadratic time
# complexity.
#
# Space Complexity: O(1)
# The algorithm uses a constant amount of extra space. We only store a few
# variables for the indices and lengths.
